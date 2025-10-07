from typing import List

def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    collected_results: List[str] = []
    temp_chars: List[str] = []
    depth_counter: int = 0
    index: int = 0

    while index < len(string_of_parentheses):
        current_char: str = string_of_parentheses[index]
        if current_char == '(':
            depth_counter += 1
            temp_chars.append(current_char)
        elif current_char == ')':
            depth_counter -= 1
            temp_chars.append(current_char)
            if depth_counter == 0:
                combined_string = ''.join(temp_chars)
                collected_results.append(combined_string)
                temp_chars.clear()
        else:
            # Ignore any other characters
            pass
        index += 1

    return collected_results