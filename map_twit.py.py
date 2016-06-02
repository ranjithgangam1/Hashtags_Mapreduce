#!/usr/bin/env python
#_*_coding:utf-8_*_
import json
import sys
import datetime

for line in sys.stdin:
  #print line
  line = json.loads(line)
  dt = datetime.datetime.strptime(line['created_at'],'%a %b %d %H:%M:%S +0000 %Y')
  #print line
  for eachhash in line['entities']['hashtags']:
    print '%s\t%s' %(dt.strftime('%a'), eachhash['text'].encode('utf-8'))
