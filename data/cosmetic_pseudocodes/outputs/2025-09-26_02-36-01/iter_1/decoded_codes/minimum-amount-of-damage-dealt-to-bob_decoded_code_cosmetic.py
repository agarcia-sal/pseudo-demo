from typing import List

class Enemy:
    def __init__(self, damage: int, timeTakenDown: int):
        self.damage = damage
        self.timeTakenDown = timeTakenDown

class Solution:
    def minDamage(self, power: int, damage: List[int], health: List[int]) -> int:
        totalDamage = 0
        damageSum = sum(damage)
        enemyList = []

        for i in range(len(damage)):
            hitsNeeded = (health[i] + power - 1) // power
            enemyList.append(Enemy(damage[i], hitsNeeded))

        # Sort by damage/timeTakenDown ratio descending
        enemyList.sort(key=lambda enemy: enemy.damage / enemy.timeTakenDown, reverse=True)

        for enemy in enemyList:
            totalDamage += damageSum * enemy.timeTakenDown
            damageSum -= enemy.damage

        return totalDamage