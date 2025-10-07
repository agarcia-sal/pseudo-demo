from functools import cmp_to_key

class Enemy:
    def __init__(self, damage, timeTakenDown):
        self.damage = damage
        self.timeTakenDown = timeTakenDown

class Solution:
    def minDamage(self, power, damage, health):
        total_damage_sum = sum(damage)
        enemies = []
        for d, h in zip(damage, health):
            time_taken_down = (h + power - 1) // power  # ceil division for time steps
            enemies.append(Enemy(d, time_taken_down))

        def comparator(a, b):
            # Sort enemies to minimize total damage taken
            val1 = a.damage * b.timeTakenDown
            val2 = b.damage * a.timeTakenDown
            if val1 > val2:
                return -1
            elif val1 < val2:
                return 1
            else:
                return 0

        enemies.sort(key=cmp_to_key(comparator))

        result = 0
        curr_total_damage = total_damage_sum
        for enemy in enemies:
            result += curr_total_damage * enemy.timeTakenDown
            curr_total_damage -= enemy.damage

        return result