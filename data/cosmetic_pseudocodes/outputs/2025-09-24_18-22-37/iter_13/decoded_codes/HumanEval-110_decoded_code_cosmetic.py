from typing import List

def exchange(list_one: List[int], list_two: List[int]) -> str:
    count_even = 0
    count_odd = 0
    iterator_index = 0

    while True:
        if iterator_index >= len(list_one):
            break
        current_value = list_one[iterator_index]
        remainder = current_value - 2 * (current_value // 2)
        if remainder == 1:
            count_odd += 1
        iterator_index += 1

    index_iterator = 0
    while True:
        if index_iterator >= len(list_two):
            break
        element_value = list_two[index_iterator]
        mod_result = element_value - 2 * (element_value // 2)
        if mod_result == 0:
            count_even += 1
        index_iterator += 1

    if not (count_even - count_odd < 0):
        return "YES"
    else:
        return "NO"