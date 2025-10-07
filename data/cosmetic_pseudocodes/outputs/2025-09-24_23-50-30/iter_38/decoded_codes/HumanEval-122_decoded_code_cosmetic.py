from typing import List, Union

def add_elements(list_values: List[Union[int, float]], value_limit: int) -> Union[int, float]:
    sum_accumulator: Union[int, float] = 0
    item_index: int = 0

    while item_index < value_limit:
        item = list_values[item_index]
        if not (len(str(item)) > 2):
            sum_accumulator += item
        item_index += 1

    return sum_accumulator