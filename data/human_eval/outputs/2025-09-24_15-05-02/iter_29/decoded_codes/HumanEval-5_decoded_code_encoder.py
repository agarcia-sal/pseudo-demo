from typing import List

def intersperse(list_of_numbers: List[int], delimiter: int) -> List[int]:
    if not list_of_numbers:
        return []
    result_list: List[int] = []
    for number in list_of_numbers[:-1]:
        result_list.append(number)
        result_list.append(delimiter)
    result_list.append(list_of_numbers[-1])
    return result_list