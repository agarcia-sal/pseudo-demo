from typing import Sequence, Union

def add_elements(sequence_n: Sequence[Union[int, float, complex]], number_p: int) -> Union[int, float, complex]:
    total_accumulator: Union[int, float, complex] = 0
    position: int = 0
    while position < number_p:
        current_item = sequence_n[position]
        if len(str(current_item)) <= 2:
            total_accumulator += current_item
        position += 1
    return total_accumulator