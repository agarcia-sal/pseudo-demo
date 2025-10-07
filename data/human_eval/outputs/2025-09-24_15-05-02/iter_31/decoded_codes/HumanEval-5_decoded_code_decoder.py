from typing import List, Union

def intersperse(list_of_numbers: List[Union[int, float]], delimiter: Union[int, float]) -> List[Union[int, float]]:
    if not list_of_numbers:
        return []
    result_list: List[Union[int, float]] = []
    for number in list_of_numbers[:-1]:
        result_list.append(number)
        result_list.append(delimiter)
    result_list.append(list_of_numbers[-1])
    return result_list