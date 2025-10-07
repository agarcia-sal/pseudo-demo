from typing import List

def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    result_collection: List[str] = []
    active_chars: List[str] = []
    depth_counter: int = 0

    def process_index(idx: int) -> None:
        if idx > len(string_of_parentheses):
            return

        curr_char = string_of_parentheses[idx - 1]  # Adjust for 0-based indexing

        if curr_char == '(':
            nonlocal depth_counter
            depth_counter += 1
            active_chars.append(curr_char)
        elif curr_char == ')':
            nonlocal depth_counter
            depth_counter -= 1
            active_chars.append(curr_char)

            if depth_counter == 0:
                result_collection.append(''.join(active_chars))
                active_chars.clear()

        process_index(idx + 1)

    process_index(1)
    return result_collection