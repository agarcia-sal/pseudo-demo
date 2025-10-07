from typing import List

def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    results_accumulator: List[str] = []
    buffer_accumulator: List[str] = []
    depth_counter: int = 0

    def process_chars(index: int) -> None:
        nonlocal depth_counter, buffer_accumulator, results_accumulator

        if index >= len(string_of_parentheses):
            return
        current_char = string_of_parentheses[index]

        if current_char == '(':
            depth_counter += 1
            buffer_accumulator.append(current_char)
        elif current_char == ')':
            depth_counter -= 1
            buffer_accumulator.append(current_char)
            if depth_counter == 0:
                combined_string = ''.join(buffer_accumulator)
                results_accumulator.append(combined_string)
                buffer_accumulator = []
        # else: ignore other characters

        process_chars(index + 1)

    process_chars(0)
    return results_accumulator