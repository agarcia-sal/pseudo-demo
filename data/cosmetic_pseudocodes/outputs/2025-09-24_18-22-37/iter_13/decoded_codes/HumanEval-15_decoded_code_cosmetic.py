from typing import List

def string_sequence(unused_param: int) -> str:
    output_parts: List[str] = []
    index_counter: int = 0
    limit_value: int = unused_param
    while True:
        current_number: int = index_counter
        stringified_number: str = str(current_number)
        output_parts.append(stringified_number)
        if index_counter == limit_value:
            break
        index_counter += 1
    final_output: str = ""
    iterator_position: int = 0
    while iterator_position < len(output_parts):
        final_output += output_parts[iterator_position]
        if iterator_position < len(output_parts) - 1:
            final_output += " "
        iterator_position += 1
    return final_output