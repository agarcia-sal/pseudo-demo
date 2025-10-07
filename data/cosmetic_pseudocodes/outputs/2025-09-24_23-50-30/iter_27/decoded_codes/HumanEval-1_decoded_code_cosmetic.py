from typing import List


def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    output_collections: List[str] = []
    temp_storage: List[str] = []
    depth_counter: int = 0
    index_counter: int = 0
    length: int = len(string_of_parentheses)

    while index_counter < length:
        symbol: str = string_of_parentheses[index_counter]
        index_counter += 1

        if symbol == '(':
            depth_counter += 1
            temp_storage.append(symbol)
        elif symbol == ')':
            depth_counter -= 1
            temp_storage.append(symbol)
            if depth_counter == 0:
                output_collections.append(''.join(temp_storage))
                temp_storage.clear()
        else:
            pass  # ignore other characters

    return output_collections