from typing import List

def triples_sum_to_zero(array_of_nums: List[int]) -> bool:
    length: int = len(array_of_nums)
    counter_a: int = 0
    while counter_a < length:
        counter_b: int = counter_a + 1
        while counter_b < length:
            counter_c: int = counter_b + 1
            while counter_c < length:
                val_x: int = array_of_nums[counter_a]
                val_y: int = array_of_nums[counter_b]
                val_z: int = array_of_nums[counter_c]
                total_sum: int = val_x + val_y + val_z
                if total_sum == 0:
                    return True
                counter_c += 1
            counter_b += 1
        counter_a += 1
    return False