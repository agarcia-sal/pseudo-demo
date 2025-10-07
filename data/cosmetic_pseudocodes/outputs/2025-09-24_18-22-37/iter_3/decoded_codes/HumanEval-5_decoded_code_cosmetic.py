from typing import List, Union

def intersperse(list_of_numbers: List[Union[int, float]], delimiter: Union[int, float]) -> List[Union[int, float]]:
    index: int = 0
    result_list: List[Union[int, float]] = []

    while index < len(list_of_numbers) - 1:
        result_list.append(list_of_numbers[index])
        result_list.append(delimiter)
        index += 1

    if len(list_of_numbers) > 0:
        result_list.append(list_of_numbers[-1])

    return result_list