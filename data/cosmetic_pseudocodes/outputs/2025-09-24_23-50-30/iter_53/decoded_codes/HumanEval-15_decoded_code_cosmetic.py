from typing import List

def string_sequence(n_value: int) -> str:
    index_tracker: int = 0
    output_accumulator: List[str] = []
    while index_tracker <= n_value:
        output_accumulator.append(str(index_tracker))
        index_tracker += 1
    result_string: str = ""
    for each_element in output_accumulator:
        if not result_string:
            result_string = each_element
        else:
            result_string += " " + each_element
    return result_string