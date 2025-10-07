from typing import List

def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    collected_groups: List[str] = []
    temp_accumulator: List[str] = []
    depth_counter: int = 0
    pos: int = 0

    while pos < len(string_of_parentheses):
        symbol: str = string_of_parentheses[pos]

        if symbol == '(':
            depth_counter += 1
            temp_accumulator.append(symbol)
            pos += 1
            continue

        if symbol == ')':
            depth_counter -= 1
            temp_accumulator.append(symbol)
            if depth_counter == 0:
                group_string = ''.join(temp_accumulator)
                collected_groups.append(group_string)
                temp_accumulator.clear()

        pos += 1

    return collected_groups