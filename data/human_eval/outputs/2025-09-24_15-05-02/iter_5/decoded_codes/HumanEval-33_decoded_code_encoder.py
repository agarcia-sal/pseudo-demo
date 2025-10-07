from typing import List

def sort_third(l: List) -> List:
    sorted_l = l[:]
    indices_divisible_by_three = [i for i in range(len(sorted_l)) if i % 3 == 0]
    sorted_values = sorted(sorted_l[i] for i in indices_divisible_by_three)
    for index, value in zip(indices_divisible_by_three, sorted_values):
        sorted_l[index] = value
    return sorted_l