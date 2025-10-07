from typing import List

def separate_paren_groups(input_sequence: str) -> List[str]:
    result_collection: List[str] = []
    buffer_accumulator: List[str] = []
    nesting_counter: int = 0

    for current_symbol in input_sequence:
        if current_symbol == ')':
            nesting_counter -= 1
            buffer_accumulator.append(current_symbol)
            if nesting_counter == 0:
                result_collection.append("".join(buffer_accumulator))
                buffer_accumulator.clear()
        elif current_symbol == '(':
            nesting_counter += 1
            buffer_accumulator.append(current_symbol)

    return result_collection