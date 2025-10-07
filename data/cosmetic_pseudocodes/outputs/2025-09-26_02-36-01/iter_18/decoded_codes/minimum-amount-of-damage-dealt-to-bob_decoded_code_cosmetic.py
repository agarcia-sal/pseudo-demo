from functools import cmp_to_key
from math import ceil

class Enemy:
    def __init__(self, damage, timeTakenDown):
        self.damage = damage
        self.timeTakenDown = timeTakenDown

class Solution:
    def minDamage(self, power, damage, health):
        totalAmount = sum(damage)

        enemyList = []
        for d, h in zip(damage, health):
            calcTime = (h + power - 1) // power
            enemyList.append(Enemy(d, calcTime))

        def ratioCompare(a, b):
            left = a.damage * b.timeTakenDown
            right = b.damage * a.timeTakenDown
            if left > right:
                return -1
            elif left < right:
                return 1
            else:
                return 0

        enemyList.sort(key=cmp_to_key(ratioCompare))

        outputValue = 0
        remSum = totalAmount
        for currentEnemy in enemyList:
            outputValue += remSum * currentEnemy.timeTakenDown
            remSum -= currentEnemy.damage

        return outputValue