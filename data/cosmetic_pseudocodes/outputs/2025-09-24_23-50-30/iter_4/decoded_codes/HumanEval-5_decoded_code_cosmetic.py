from typing import List, Union

def intersperse(list_of_numbers: List[int], delimiter: int) -> List[int]:
    def helper(index: int, acc: List[int]) -> List[int]:
        if index >= len(list_of_numbers) - 1:
            return acc + [list_of_numbers[index]]
        else:
            return helper(index + 1, acc + [list_of_numbers[index], delimiter])
    return [] if len(list_of_numbers) == 0 else helper(0, [])