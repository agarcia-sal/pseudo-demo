from functools import cmp_to_key

class Enemy:
    def __init__(self, damage, timeTakenDown):
        self.damage = damage
        self.timeTakenDown = timeTakenDown

class Solution:
    def minDamage(self, power, damage, health):
        totalDamageAccum = 0
        damageSum = 0
        enemyList = []

        idx = 0
        while idx < len(damage):
            damageSum += damage[idx]
            idx += 1

        counter = 0
        while counter < len(damage):
            dmgAtPos = damage[counter]
            hpAtPos = health[counter]

            numerator = hpAtPos + power - 1
            timeUnits = numerator // power

            foe = Enemy(dmgAtPos, timeUnits)
            enemyList.append(foe)
            counter += 1

        def comparator(a, b):
            valA = a.damage / a.timeTakenDown
            valB = b.damage / b.timeTakenDown
            if valA > valB:
                return -1  # return -1 to sort descending by valA
            elif valA < valB:
                return 1
            else:
                return 0

        enemyList.sort(key=cmp_to_key(comparator))

        iterator = 0
        while iterator < len(enemyList):
            currentEnemy = enemyList[iterator]

            addVal = damageSum * currentEnemy.timeTakenDown
            totalDamageAccum += addVal

            damageSum -= currentEnemy.damage

            iterator += 1

        return totalDamageAccum