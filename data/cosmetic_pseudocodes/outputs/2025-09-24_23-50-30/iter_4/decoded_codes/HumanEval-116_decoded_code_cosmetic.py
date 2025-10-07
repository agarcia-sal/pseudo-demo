from typing import List

def sort_array(array_of_integers: List[int]) -> List[int]:
    def count_ones(n: int, total: int) -> int:
        if n == 0:
            return total
        return count_ones(n // 2, total + (n % 2))

    def by_ones(x: int) -> int:
        return count_ones(x, 0)

    temp_sorted: List[int] = array_of_integers[:]
    index: int = 0

    while index < len(temp_sorted) - 1:
        if temp_sorted[index] > temp_sorted[index + 1]:
            temp_sorted[index], temp_sorted[index + 1] = temp_sorted[index + 1], temp_sorted[index]
            index = 0
        else:
            index += 1

    final_result: List[int] = []
    while temp_sorted:
        min_value = temp_sorted[0]
        for element in temp_sorted:
            by_ones_element = by_ones(element)
            by_ones_min = by_ones(min_value)
            if by_ones_element < by_ones_min or (by_ones_element == by_ones_min and element < min_value):
                min_value = element
        final_result.append(min_value)
        temp_sorted.remove(min_value)

    return final_result