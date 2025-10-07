from typing import List

def move_one_ball(array_of_integers: List[int]) -> bool:
    if not array_of_integers:
        return True
    sorted_version = sorted(array_of_integers)
    min_val = min(array_of_integers)
    min_pos = array_of_integers.index(min_val)
    shifted_array = array_of_integers[min_pos:] + array_of_integers[:min_pos]
    return all(shifted_array[i] == sorted_version[i] for i in range(len(array_of_integers)))