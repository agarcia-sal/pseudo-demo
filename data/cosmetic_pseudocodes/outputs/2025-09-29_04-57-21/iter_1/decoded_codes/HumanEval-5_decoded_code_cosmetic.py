from typing import List


def intersperse(list_of_numbers: List[int], delimiter: int) -> List[int]:
    length = len(list_of_numbers)
    if length == 0:
        return []
    output: List[int] = []
    index = 0
    while index < length - 1:
        output.append(list_of_numbers[index])
        output.append(delimiter)
        index += 1
    output.append(list_of_numbers[length - 1])
    return output