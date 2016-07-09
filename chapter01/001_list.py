#!/usr/bin/env python
# encoding: utf-8

bob = ['Bob Smith',42,30000,'Software']

sue = ['Sue Jones',22,25000,'Hardtware']

people = [bob,sue]
for person in people:
    print person[0].split()[-1]
    person[2]*=1.20

    print person[2]

pays = map(lambda x: x[2],people)
print pays
print type(pays)

pays = sum(person[2] for person in people)
print '所有人的薪水之和为：',pays

print '增加一条数据！！！'
people.append(['Andy Lau',50,40000,'Singer'])
print '所有员工的总数为：',len(people)

