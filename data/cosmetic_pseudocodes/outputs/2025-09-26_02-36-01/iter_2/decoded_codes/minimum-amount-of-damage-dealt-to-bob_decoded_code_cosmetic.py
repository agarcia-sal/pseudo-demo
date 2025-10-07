from typing import List

class Enemy:
    def __init__(self, dmg: int, downTime: int):
        self.damage = dmg
        self.timeTakenDown = downTime

class Solution:
    def minDamage(self, power: int, damage: List[int], health: List[int]) -> int:
        totalDamageAccrued = 0
        damageSum = sum(damage)

        foes = []
        for dmg, hp in zip(damage, health):
            stepsNeeded = (hp + power - 1) // power
            foes.append(Enemy(dmg, stepsNeeded))

        foes.sort(key=lambda e: e.damage / e.timeTakenDown, reverse=True)

        for enemy in foes:
            totalDamageAccrued += damageSum * enemy.timeTakenDown
            damageSum -= enemy.damage

        return totalDamageAccrued