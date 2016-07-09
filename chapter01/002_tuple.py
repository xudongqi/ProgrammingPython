#!/usr/bin/env python
# encoding: utf-8

bob = [['name','Bob Smith'],['age',42],['pay','10000']]
sue = [['name','Sue Jones'],['age',24],['pay','12000']]

def field(record, label):
    for (fname,fvaule) in record:
        if fname == label:
            print fvaule

field(sue,'pay')

