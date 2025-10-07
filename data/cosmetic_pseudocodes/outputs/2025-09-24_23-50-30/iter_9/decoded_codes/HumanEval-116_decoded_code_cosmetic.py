from typing import List

def sort_array(numbers: List[int]) -> List[int]:
    intermediary_list: List[int] = sorted(numbers)

    def compare_key(value: int) -> int:
        binary_string: str = bin(value)[2:]
        return binary_string.count('1')

    result: List[int] = sorted(intermediary_list, key=compare_key)
    return result