#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys
readin=sys.stdin.readline
def readnums():
	return list(map(int,readin().split()))

a=readnums()
b=readnums()
if(sum(map(lambda x,y:abs(x-y),a,b))==3):
	print('NO')
else:
	print('YES')
