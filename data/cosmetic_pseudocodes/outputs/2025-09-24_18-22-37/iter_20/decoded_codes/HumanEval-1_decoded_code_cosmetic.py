from typing import List

def separate_paren_groups(input_sequence: str) -> List[str]:
    accumulator_output: List[str] = []
    buffer_segment: List[str] = []
    depth_counter: int = 0

    index_tracker: int = 0
    length_seq: int = len(input_sequence)

    while index_tracker < length_seq:
        current_symbol: str = input_sequence[index_tracker]

        if current_symbol == '(':
            depth_counter += 1
            buffer_segment.append(current_symbol)
        elif current_symbol == ')':
            depth_counter -= 1
            buffer_segment.append(current_symbol)

            if depth_counter == 0:
                combined_string: str = ''.join(buffer_segment)
                accumulator_output.append(combined_string)
                buffer_segment = []
        else:
            # Ignore any characters other than '(' or ')'
            pass

        index_tracker += 1

    return accumulator_output