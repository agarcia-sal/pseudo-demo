from typing import List

def triples_sum_to_zero(numbers: List[int]) -> bool:
    length = len(numbers)
    position_a = 0
    while position_a <= length - 1:
        position_b = position_a + 1
        while position_b <= length - 1:
            position_c = position_b + 1
            while position_c <= length - 1:
                first_element = numbers[position_a]
                second_element = numbers[position_b]
                third_element = numbers[position_c]
                sum_parts = first_element + second_element + third_element
                if sum_parts == 0:
                    return True
                position_c += 1
            position_b += 1
        position_a += 1
    return False