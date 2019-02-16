#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib, json, requests, time, random, configs, threading

def send_message(text, chat_id, com):
    requests.get(com.url + "sendMessage?text={}&chat_id={}".format(urllib.quote_plus(text), chat_id)).content.decode("utf8")

class Communication:
    def __init__(self, configurations=None):
        self.msg_proc_list = []
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
        return self.__get_json_from_url(url)

    def get_last_chat_id_and_text(self, updates):
        text = None
        chat_id = None
        update_id = None
        group_title = None

        if len(updates["result"]) > 0:
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

        return (text, chat_id, group_title, update_id)

    def on_receive_msg(self, func):
        self.msg_proc_list.append(func)

    def event_loop(self):
        update_id = None
        while True:
            text, chat_id, group_title, update_id = self.get_last_chat_id_and_text(self.get_updates(update_id))
            if update_id and (text <> None) and (len(text) > 0):
                update_id = update_id + 1
                for f in self.msg_proc_list:
                    f(text, chat_id, group_title, self)

    def start(self):
        event_loop_thread = threading.Thread(target=self.event_loop)
        self.threads.append(event_loop_thread)
        event_loop_thread.start()
