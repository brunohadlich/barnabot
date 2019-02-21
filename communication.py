#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib, json, requests, time, random, configs, threading, datetime, pytz

def send_message(text, chat_id, com):
    return requests.get(com.url + "sendMessage?text={}&chat_id={}".format(urllib.parse.quote_plus(text), chat_id)).content.decode("utf8")

class Communication:
    def __init__(self, configurations=None):
        self.msg_proc_list = []
        self.scheduled_msgs = []
        self.scheduled_every_day_msgs = []
        self.threads = []
        self.load_configs(configurations)

    def load_configs(self, configurations=None):
        if not configurations:
            configurations = configs.load()
        if not "token" in configurations:
            raise Exception("'token' not found on loaded configurations.")

        if not "req_updates_timeout_sec" in configurations:
            raise Exception("'req_updates_timeout_sec' not found on loaded configurations.")

        self.token = configurations["token"]
        self.req_updates_timeout_sec = configurations["req_updates_timeout_sec"]
        self.url = "https://api.telegram.org/bot{}/".format(configurations["token"])

    def __get_url(self, url):
        return requests.get(url).content.decode("utf8")

    def __get_json_from_url(self, url):
        return json.loads(self.__get_url(url))

    def get_updates(self, offset=None):
        url = self.url + "getUpdates?timeout={}".format(str(self.req_updates_timeout_sec))
        if offset:
            url += "&offset={}".format(offset)
        print("get_updates {}".format(url))
        return self.__get_json_from_url(url)

    def get_last_chat_id_and_text(self, updates):
        message = None
        text = None
        chat_id = None
        update_id = None
        group_title = None

        if len(updates["result"]) > 0:
            print(updates["result"][0])
            if 'message' in updates["result"][0]:
                message = updates["result"][0]["message"]
                #There are updates that notify the bot was added to a group, in
                #this case the text is empty and we have to check it
                if "text" in message:
                    text = message["text"]
                    chat_id = message["chat"]["id"]
                    if message["chat"]["type"] == "group":
                        group_title =message["chat"]["title"]
                else:
                    text = ""
            update_id = updates["result"][0]["update_id"]

        return (message, text, chat_id, group_title, update_id)

    def on_receive_msg(self, func):
        self.msg_proc_list.append(func)

    def event_loop(self):
        update_id = None
        while True:
            message, text, chat_id, group_title, update_id = self.get_last_chat_id_and_text(self.get_updates(update_id))
            if update_id:
                if (text != None) and (len(text) > 0):
                    for f in self.msg_proc_list:
                        f(message, text, chat_id, group_title, self)
                update_id = update_id + 1

    def run_scheduled_msgs(self):
        ELAPSE_TIME=60
        while True:
            for sch in self.scheduled_msgs:
                sch_time = sch[0]
                msg = sch[1]
                chat_id = sch[2]
                now = datetime.datetime.now(tz=pytz.utc)
                now = now.astimezone(pytz.timezone(sch_time.tzinfo.zone))
                missing_time = (sch_time - now).seconds
                print('Missing {} seconds to send msg "{}" for chat_id {}.'.format(str(missing_time), msg, str(chat_id)))
                if missing_time <= ELAPSE_TIME:
                    send_message(msg, chat_id, self)
            time.sleep(ELAPSE_TIME)

    def run_scheduled_every_day_msgs(self):
        ELAPSE_TIME=60
        while True:
            for sch in self.scheduled_every_day_msgs:
                sch_time = sch[0]
                msg = sch[1]
                chat_id = sch[2]
                now = datetime.datetime.now(tz=pytz.utc)
                now = now.astimezone(pytz.timezone(sch_time.tzinfo.zone))
                sch_time = sch_time.replace(year=now.year, month=now.month, day=now.day)
                missing_time = (sch_time - now).seconds
                print('Missing {} seconds to send msg "{}" for chat_id {}.'.format(str(missing_time), msg, str(chat_id)))
                if (missing_time <= ELAPSE_TIME) and (now.weekday() < 5):
                    send_message(msg, chat_id, self)
            time.sleep(ELAPSE_TIME)

    def start(self):
        event_loop_thread = threading.Thread(target=self.event_loop)
        self.threads.append(event_loop_thread)
        event_loop_thread.start()

        scheduled_msgs_thread = threading.Thread(target=self.run_scheduled_msgs)
        self.threads.append(scheduled_msgs_thread)
        scheduled_msgs_thread.start()

        scheduled_every_day_msgs_thread = threading.Thread(target=self.run_scheduled_every_day_msgs)
        self.threads.append(scheduled_every_day_msgs_thread)
        scheduled_every_day_msgs_thread.start()

    #date_time is an argument that must have its timezone set to UTC for sake of correct execution
    def schedule_msg(self, date_time, msg, chat_id):
       self.scheduled_msgs.append((date_time, msg, chat_id))

    #date_time is an argument that must have its timezone set to UTC for sake of correct execution
    def schedule_every_day_msg(self, date_time, msg, chat_id):
       self.scheduled_every_day_msgs.append((date_time, msg, chat_id))
