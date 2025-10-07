from typing import List

def intersperse(list_of_numbers: List[int], delimiter: int) -> List[int]:
    if not list_of_numbers:
        return []
    result: List[int] = []

    def helper(flag: bool, index: int) -> List[int]:
        if flag and index < len(list_of_numbers) - 1:
            result.append(list_of_numbers[index])
            result.append(delimiter)
            return helper(True, index + 1)
        if flag and index == len(list_of_numbers) - 1:
            return result + [list_of_numbers[index]]
        return []

    return helper(True, 0)