#!/usr/bin/env python
# encoding: utf-8

andy = dict(name = 'Andy Xu',age=49,pay=30000,job='dev')
jack= dict(name = 'Jack Zhang',age=49,pay=32000,job='it')
db = {}
db['andy'] = andy
db['jack'] = jack

print db

for record in db.values():
    print record['pay']

print [rec['name'] for rec in db.values() if rec['pay'] > 30000]
