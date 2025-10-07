class Enemy:
    def __init__(self, damage, timeTakenDown):
        self.damage = damage
        self.timeTakenDown = timeTakenDown


class Solution:
    def minDamage(self, power, damage, health):
        totalSum = 0
        counter = 0
        while counter < len(damage):
            totalSum += damage[counter]
            counter += 1

        result = 0
        enemyList = []

        idx = 0
        while idx != len(damage):
            dmgVal = damage[idx]
            hlthVal = health[idx]
            divResult = (hlthVal + (power - 1)) // power
            enemyList.append(Enemy(dmgVal, divResult))
            idx += 1

        def compareRatio(a, b):
            ratioA = a.damage / a.timeTakenDown
            ratioB = b.damage / b.timeTakenDown
            return ratioA > ratioB

        def sortEnemiesDescending(arr):
            n = len(arr)
            i = 0
            while True:
                swapped = False
                j = 0
                while j < n - i - 1:
                    if not compareRatio(arr[j], arr[j + 1]):
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
                        swapped = True
                    j += 1
                i += 1
                if not swapped or i >= n:
                    break

        sortEnemiesDescending(enemyList)

        iterator = 0
        while True:
            if iterator >= len(enemyList):
                break
            currentEnemy = enemyList[iterator]
            addition = totalSum * currentEnemy.timeTakenDown
            result += addition
            totalSum -= currentEnemy.damage
            iterator += 1

        return result