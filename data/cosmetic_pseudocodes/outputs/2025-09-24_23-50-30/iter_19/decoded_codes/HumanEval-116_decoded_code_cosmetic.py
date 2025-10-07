from typing import List, Callable

def sort_array(data: List[int]) -> List[int]:
    step_one: List[int] = []
    for element in data:
        step_one.append(element)
    step_two: List[int] = step_one.copy()
    step_two.sort()  # sort step_two in-place

    def key_function(item: int) -> int:
        binary_string: str = bin(item)[2:]  # convert to binary string without '0b' prefix
        bit_count: int = sum(1 for bit_char in binary_string if bit_char == '1')
        return bit_count

    return sorted(step_two, key=key_function)