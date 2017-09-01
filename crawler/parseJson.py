#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
from pprint import pprint

with open('test.json') as data_file:
    data = json.load(data_file)

for item in data:
    print "%s    %s"%(item['house_id'], item['title'])
