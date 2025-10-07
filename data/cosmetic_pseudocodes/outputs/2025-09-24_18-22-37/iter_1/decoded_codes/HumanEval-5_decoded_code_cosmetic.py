from typing import List, Union

def intersperse(list_of_numbers: List[Union[int, float]], delimiter: Union[int, float]) -> List[Union[int, float]]:
    if not list_of_numbers:
        return []
    output: List[Union[int, float]] = []
    last_index = len(list_of_numbers) - 1
    for i in range(last_index):
        output.append(list_of_numbers[i])
        output.append(delimiter)
    output.append(list_of_numbers[last_index])
    return output