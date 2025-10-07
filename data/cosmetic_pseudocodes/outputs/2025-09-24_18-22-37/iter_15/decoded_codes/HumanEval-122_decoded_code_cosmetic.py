from typing import Sequence, Union

def add_elements(vectors: Sequence[Union[int, float]], factor: int) -> Union[int, float]:
    accumulator: Union[int, float] = 0
    counter: int = 0
    while counter < factor:
        current_item = vectors[counter]
        string_form = str(current_item)
        string_length = len(string_form)
        if string_length <= 2:
            accumulator += current_item
        counter += 1
    return accumulator