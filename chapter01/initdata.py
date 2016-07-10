#!/usr/bin/env python
# encoding: utf-8

bob = {'name':'Bob Smith','age':21,'pay':30000,'job':'dev'}
andy = {'name':'Andy Xu','age':31,'pay':50000,'job':'devops'}
jack = {'name':'Jack Fang','age':41,'pay':35000,'job':'hdw'}

db = {}
db['bob'] = bob
db['andy'] = andy
db['jack'] = jack

if __name__ == '__main__':
    for key in db:
        print key,'=>\n',db[key]
