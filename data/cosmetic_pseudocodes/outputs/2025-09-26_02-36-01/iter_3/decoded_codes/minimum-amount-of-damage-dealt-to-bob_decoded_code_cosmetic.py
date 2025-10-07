class Enemy:
    def __init__(self, damage, timeTakenDown):
        self.damage = damage
        self.timeTakenDown = timeTakenDown


class Solution:
    def minDamage(self, power, damage, health):
        result_accumulator = 0
        total_damage_sum = 0
        iterator_index = 0
        while iterator_index < len(damage):
            total_damage_sum += damage[iterator_index]
            iterator_index += 1

        enemy_collection = []

        loop_counter = 0
        while loop_counter < len(damage):
            dmg_var = damage[loop_counter]
            hp_var = health[loop_counter]
            time_down_value = (hp_var + (power - 1)) // power

            enemy_instance = Enemy(dmg_var, time_down_value)
            enemy_collection.append(enemy_instance)
            loop_counter += 1

        def ratio_compare(enemy_obj):
            return enemy_obj.damage / enemy_obj.timeTakenDown

        enemy_collection = sorted(enemy_collection, key=ratio_compare, reverse=True)

        index_var = 0
        while index_var < len(enemy_collection):
            current_enemy = enemy_collection[index_var]
            increment_value = total_damage_sum * current_enemy.timeTakenDown
            result_accumulator += increment_value
            total_damage_sum -= current_enemy.damage
            index_var += 1

        return result_accumulator