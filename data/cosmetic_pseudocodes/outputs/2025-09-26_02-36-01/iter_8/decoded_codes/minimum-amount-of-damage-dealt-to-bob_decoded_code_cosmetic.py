class Enemy:
    def __init__(self, damage, timeTakenDown):
        self.damage = damage
        self.timeTakenDown = timeTakenDown


class Solution:
    def minDamage(self, power, damage, health):
        total_damage_taken = 0
        total_damage = 0
        n = 0
        enemies = []

        def _sumList(lst):
            s = 0
            i = 0
            while i < len(lst):
                s += lst[i]
                i += 1
            return s

        total_damage = _sumList(damage)
        n = 0
        while n < len(damage):
            dmg = damage[n]
            hp = health[n]
            hits = (hp + power - 1) // power  # number of hits to take down this enemy
            enemy = Enemy(dmg, hits)
            enemies.append(enemy)
            n += 1

        def _compareEnemies(a, b):
            left = a.damage * b.timeTakenDown
            right = b.damage * a.timeTakenDown
            if left < right:
                return 1
            elif left > right:
                return -1
            else:
                return 0

        swapped = True
        while swapped:
            swapped = False
            i = 0
            while i < len(enemies) - 1:
                if _compareEnemies(enemies[i], enemies[i + 1]) > 0:
                    enemies[i], enemies[i + 1] = enemies[i + 1], enemies[i]
                    swapped = True
                i += 1

        idx = 0
        while True:
            if idx >= len(enemies):
                break
            enemy = enemies[idx]
            total_damage_taken += total_damage * enemy.timeTakenDown
            total_damage -= enemy.damage
            idx += 1

        return total_damage_taken