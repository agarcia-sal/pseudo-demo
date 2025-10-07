class Enemy:
    def __init__(self, damage, timeTakenDown):
        self.damage = damage
        self.timeTakenDown = timeTakenDown

class Solution:
    def minDamage(self, power, damage, health):
        total_damage = 0
        index = 0
        enemies = []

        # Sum of all damage values
        def sum_damage(dmg_list):
            total = 0
            for d in dmg_list:
                total += d
            return total

        total_power = sum_damage(damage)

        # Create Enemy instances with computed timeTakenDown
        while index < len(damage):
            dmg = damage[index]
            hp = health[index]
            # Number of hits needed to take down enemy
            time_taken = (hp + (power - 1)) // power  # ceil division
            enemies.append(Enemy(dmg, time_taken))
            index += 1

        # Sort enemies in descending order by damage/timeTakenDown ratio
        def sort_enemies_by_ratio(lst):
            for i in range(1, len(lst)):
                j = i
                while j > 0 and (lst[j].damage / lst[j].timeTakenDown) > (lst[j-1].damage / lst[j-1].timeTakenDown):
                    lst[j], lst[j-1] = lst[j-1], lst[j]
                    j -= 1

        sort_enemies_by_ratio(enemies)

        # Calculate total damage
        while len(enemies) > 0:
            current = enemies.pop(0)
            total_damage += total_power * current.timeTakenDown
            total_power -= current.damage

        return total_damage