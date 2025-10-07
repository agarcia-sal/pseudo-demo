from typing import Sequence

def concatenate(input_sequence: Sequence[str]) -> str:
    output_string: str = ""
    for element_in_sequence in input_sequence:
        output_string += element_in_sequence
    return output_string