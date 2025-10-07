from typing import List

def separate_paren_groups(input_string: str) -> List[str]:
    results_accumulator: List[str] = []
    temp_storage: List[str] = []
    nesting_level: int = 0
    index_counter: int = 0
    input_length: int = len(input_string)

    while index_counter < input_length:
        current_char = input_string[index_counter]

        if current_char == '(':
            nesting_level += 1
            temp_storage.append(current_char)
        elif current_char == ')':
            nesting_level -= 1
            temp_storage.append(current_char)
            if nesting_level == 0:
                combined_string = ''.join(temp_storage)
                results_accumulator.append(combined_string)
                temp_storage.clear()
        # else: do nothing
        index_counter += 1

    return results_accumulator