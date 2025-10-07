from typing import List

def intersperse(list_of_numbers: List[int], delimiter: int) -> List[int]:
    if len(list_of_numbers) == 0:
        return []
    result_list: List[int] = []
    for index in range(len(list_of_numbers) - 1):
        result_list.append(list_of_numbers[index])
        result_list.append(delimiter)
    result_list.append(list_of_numbers[-1])
    return result_list