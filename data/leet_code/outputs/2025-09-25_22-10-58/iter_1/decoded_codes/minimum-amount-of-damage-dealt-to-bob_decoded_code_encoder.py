from typing import List

class Enemy:
    def __init__(self, damage: int, timeTakenDown: int):
        self.damage = damage
        self.timeTakenDown = timeTakenDown

class Solution:
    def minDamage(self, power: int, damage: List[int], health: List[int]) -> int:
        ans = 0
        sumDamage = sum(damage)
        enemies = []
        for i in range(len(damage)):
            current_damage = damage[i]
            current_health = health[i]
            time_taken = (current_health + power - 1) // power  # ceiling division for time to take down
            enemies.append(Enemy(current_damage, time_taken))
        # Sort enemies by damage/timeTakenDown in descending order
        enemies.sort(key=lambda e: e.damage / e.timeTakenDown, reverse=True)
        for enemy in enemies:
            ans += sumDamage * enemy.timeTakenDown
            sumDamage -= enemy.damage
        return ans