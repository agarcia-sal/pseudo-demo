from typing import List

def make_a_pile(qwerty: int) -> List[int]:
    output_list: List[int] = []
    temp_index: int = 0
    while temp_index <= qwerty - 1:
        temp_value: int = 0
        temp_value = qwerty
        temp_mul: int = 0
        temp_mul = temp_index * 2
        temp_value = temp_value + temp_mul
        output_list.append(temp_value)
        temp_index += 1
    return output_list