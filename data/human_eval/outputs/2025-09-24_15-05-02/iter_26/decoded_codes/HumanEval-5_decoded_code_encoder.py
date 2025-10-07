from typing import List, Union

def intersperse(list_of_numbers: List[Union[int, float]], delimeter: Union[int, float]) -> List[Union[int, float]]:
    if not list_of_numbers:
        return []

    result: List[Union[int, float]] = []
    for number in list_of_numbers[:-1]:
        result.append(number)
        result.append(delimeter)
    result.append(list_of_numbers[-1])
    return result