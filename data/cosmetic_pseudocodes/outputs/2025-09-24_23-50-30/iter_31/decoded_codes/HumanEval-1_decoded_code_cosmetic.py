from typing import List


def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    output_collection: List[str] = []
    temporary_buffer: List[str] = []
    nesting_counter: int = 0

    def process_index(current_index: int) -> None:
        nonlocal nesting_counter, temporary_buffer, output_collection
        if current_index == len(string_of_parentheses):
            return
        symbol = string_of_parentheses[current_index]
        if symbol == '(':
            nesting_counter += 1
            temporary_buffer.append(symbol)
        elif symbol == ')':
            nesting_counter -= 1
            temporary_buffer.append(symbol)
            if nesting_counter == 0:
                output_collection.append(''.join(temporary_buffer))
                temporary_buffer.clear()
        # else: no operation for other symbols
        process_index(current_index + 1)

    process_index(0)
    return output_collection