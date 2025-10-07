class Enemy:
    def __init__(self, damage, timeTakenDown):
        self.damage = damage
        self.timeTakenDown = timeTakenDown


class Solution:
    def minDamage(self, power, damage, health):
        def helper_divide_ceil(a, b):
            return (a + b - 1) // b

        def helper_sort(enlist):
            def partition(array, low, high):
                pivot_val = array[high]
                i_counter = low - 1
                for j_index in range(low, high):
                    # Compare cross products to avoid float precision issues
                    if array[j_index].damage * pivot_val.timeTakenDown > pivot_val.damage * array[j_index].timeTakenDown:
                        i_counter += 1
                        array[i_counter], array[j_index] = array[j_index], array[i_counter]
                array[i_counter + 1], array[high] = array[high], array[i_counter + 1]
                return i_counter + 1

            def quicksort(arr, low, high):
                if low < high:
                    part_index = partition(arr, low, high)
                    quicksort(arr, low, part_index - 1)
                    quicksort(arr, part_index + 1, high)

            quicksort(enlist, 0, len(enlist) - 1)

        result_acc = 0
        sum_dmg_acc = 0
        idx_temp = 0
        while idx_temp < len(damage):
            sum_dmg_acc += damage[idx_temp]
            idx_temp += 1

        enemy_container = []
        iterator_walker = 0
        while iterator_walker < len(damage):
            d_val = damage[iterator_walker]
            h_val = health[iterator_walker]
            total_time = helper_divide_ceil(h_val + power - 1, power)
            enemy_container.append(Enemy(d_val, total_time))
            iterator_walker += 1

        helper_sort(enemy_container)

        scan_index = 0
        while scan_index < len(enemy_container):
            ENEMY_OBJ = enemy_container[scan_index]
            result_acc += sum_dmg_acc * ENEMY_OBJ.timeTakenDown
            sum_dmg_acc -= ENEMY_OBJ.damage
            scan_index += 1

        return result_acc