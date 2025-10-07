from typing import List

def triples_sum_to_zero(array_elements: List[int]) -> bool:
    length = len(array_elements)
    position_one = 0
    while position_one < length:
        position_two = position_one + 1
        while position_two < length:
            position_three = position_two + 1
            while position_three < length:
                total_sum = array_elements[position_one] + array_elements[position_two] + array_elements[position_three]
                if total_sum == 0:
                    return True
                position_three += 1
            position_two += 1
        position_one += 1
    return False