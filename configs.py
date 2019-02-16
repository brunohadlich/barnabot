#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

def load(file_name="balde.json"):
    try:
        with open(file_name) as configs_json:
            configs = json.load(configs_json)
    except:
        raise Exception("Not able to load {}.".format(file_name))

    return configs
