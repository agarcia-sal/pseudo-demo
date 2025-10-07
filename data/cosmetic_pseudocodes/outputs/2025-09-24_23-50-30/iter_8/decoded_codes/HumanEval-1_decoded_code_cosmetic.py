from typing import List

def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    results_list: List[str] = []
    temp_collection: List[str] = []
    depth_counter: int = 0
    index_counter: int = 0

    while index_counter < len(string_of_parentheses):
        current_char: str = string_of_parentheses[index_counter]
        if current_char == '(':
            depth_counter += 1
            temp_collection.append(current_char)
        elif current_char == ')':
            depth_counter -= 1
            temp_collection.append(current_char)
            if depth_counter == 0:
                results_list.append("".join(temp_collection))
                temp_collection = []
        index_counter += 1

    return results_list