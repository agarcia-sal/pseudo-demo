class Enemy:
    def __init__(self, damage, timeTakenDown):
        self.damage = damage
        self.timeTakenDown = timeTakenDown


class Solution:
    def minDamage(self, power, damage, health):
        totalDamageSum = 0
        enemyList = []

        def sumList(numbers, idx):
            if idx >= len(numbers):
                return 0
            return numbers[idx] + sumList(numbers, idx + 1)

        totalDamageSum = sumList(damage, 0)

        def buildEnemies(i):
            if i < len(damage):
                dmgVal = damage[i]
                hpVal = health[i]
                timeCount = (hpVal + power - 1) // power
                newEnemy = Enemy(dmgVal, timeCount)
                enemyList.append(newEnemy)
                buildEnemies(i + 1)

        buildEnemies(0)

        def compareRatio(a, b):
            return (a.damage * b.timeTakenDown) > (b.damage * a.timeTakenDown)

        def sortDescending(lst):
            if len(lst) <= 1:
                return lst
            pivot = lst[0]
            leftSide = []
            rightSide = []
            idx = 1
            while idx < len(lst):
                if compareRatio(lst[idx], pivot):
                    leftSide.append(lst[idx])
                else:
                    rightSide.append(lst[idx])
                idx += 1
            return sortDescending(leftSide) + [pivot] + sortDescending(rightSide)

        enemyList = sortDescending(enemyList)

        def processEnemies(lst, accAns, accSumDamage, pos):
            if pos < len(lst):
                enemyObj = lst[pos]
                incrementVal = accSumDamage * enemyObj.timeTakenDown
                newAns = accAns + incrementVal
                newSumDamage = accSumDamage - enemyObj.damage
                return processEnemies(lst, newAns, newSumDamage, pos + 1)
            return accAns

        accumulatedResult = processEnemies(enemyList, 0, totalDamageSum, 0)

        return accumulatedResult