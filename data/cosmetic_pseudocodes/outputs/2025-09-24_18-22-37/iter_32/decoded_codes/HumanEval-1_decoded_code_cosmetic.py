from typing import List

def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    results_collection: List[str] = []
    temp_chars: List[str] = []
    depth_counter: int = 0

    index_cursor: int = 0
    length: int = len(string_of_parentheses)
    while index_cursor < length:
        current_symbol: str = string_of_parentheses[index_cursor]

        if current_symbol not in ('(', ')'):
            index_cursor += 1
            continue

        if current_symbol == '(':
            depth_counter += 1
            temp_chars.append(current_symbol)
        else:
            depth_counter -= 1
            temp_chars.append(current_symbol)

            if depth_counter == 0:
                combined_string: str = ''
                position: int = 0
                while position < len(temp_chars):
                    combined_string += temp_chars[position]
                    position += 1

                results_collection.append(combined_string)
                temp_chars.clear()

        index_cursor += 1

    return results_collection