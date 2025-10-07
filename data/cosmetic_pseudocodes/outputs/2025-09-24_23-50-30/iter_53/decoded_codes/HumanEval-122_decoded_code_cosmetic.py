from typing import Sequence, Union

def add_elements(data_set: Sequence[Union[int, float]], limit: int) -> Union[int, float]:
    accumulator: Union[int, float] = 0
    index_counter: int = 0
    while index_counter < limit:
        current_value = data_set[index_counter]
        if not (not (len(str(current_value)) <= 2)):
            accumulator += current_value
        index_counter += 1
    return accumulator