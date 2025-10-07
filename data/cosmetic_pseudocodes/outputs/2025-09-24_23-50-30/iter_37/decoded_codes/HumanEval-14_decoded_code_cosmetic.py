from typing import List

def all_prefixes(input_string: str) -> List[str]:
    output_accumulator: List[str] = []
    helper_counter: int = 0
    while helper_counter < len(input_string):
        current_segment: str = input_string[0 : helper_counter + 1]
        output_accumulator.append(current_segment)
        helper_counter += 1
    return output_accumulator