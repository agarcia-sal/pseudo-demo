from typing import List

def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    result_collection: List[str] = []
    temp_chars: List[str] = []
    depth_counter: int = 0
    index_counter: int = 0
    length_counter: int = len(string_of_parentheses)

    while index_counter < length_counter:
        current_symbol: str = string_of_parentheses[index_counter]

        if current_symbol == '(':
            depth_counter += 1
            temp_chars.append(current_symbol)
        else:
            if current_symbol == ')':
                depth_counter -= 1
                temp_chars.append(current_symbol)

                if depth_counter == 0:
                    combined_string: str = ""
                    pos: int = 0
                    temp_length: int = len(temp_chars)
                    while pos < temp_length:
                        combined_string += temp_chars[pos]
                        pos += 1
                    result_collection.append(combined_string)
                    temp_chars = []
        index_counter += 1

    return result_collection