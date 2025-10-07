from typing import List

def intersperse(list_of_numbers: List[int], delimiter: int) -> List[int]:
    if list_of_numbers:
        def helper(index: int, acc: List[int]) -> List[int]:
            if index == len(list_of_numbers) - 1:
                return acc + [list_of_numbers[index]]
            else:
                return helper(index + 1, acc + [list_of_numbers[index], delimiter])
        return helper(0, [])
    else:
        return []