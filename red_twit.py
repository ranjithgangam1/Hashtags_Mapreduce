#!/usr/bin/env python

import sys
import collections

hash_dict = {}

for line in sys.stdin:
  line = line.split('\t')
  day = line[0]
  hashword = line[1]
  if day in hash_dict.keys():
    if hashword in hash_dict[day].keys():
      hash_dict[day][hashword]+=1
    else:
      hash_dict[day][hashword] = 1
  else:
    hash_dict[day] = {}
    hash_dict[day][hashword] = 1

print '*****************************'
for eachday in hash_dict.keys():
  hash_dict[eachday] = collections.OrderedDict(sorted(hash_dict[eachday].items(), key = lambda t: t[1], reverse = 1))
 
for eachhw in hash_dict.keys():
  print eachhw,hash_dict[eachhw].items()[0]
