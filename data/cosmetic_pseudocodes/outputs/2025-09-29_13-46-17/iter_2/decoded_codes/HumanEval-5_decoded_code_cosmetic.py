from typing import List


def intersperse(list_of_numbers: List[int], delimiter: int) -> List[int]:
    def helper(idx: int, res: List[int]) -> List[int]:
        if idx > len(list_of_numbers):
            return res
        elif idx == len(list_of_numbers):
            return res + [list_of_numbers[idx]]
        else:
            return helper(idx + 1, res + [list_of_numbers[idx], delimiter])

    if len(list_of_numbers) == 0:
        return []
    else:
        return helper(1, [list_of_numbers[0]])