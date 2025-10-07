from typing import List

def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    grouped_results: List[str] = []
    temp_buffer: List[str] = []
    nesting_level: int = 0

    index_position: int = 0
    while index_position < len(string_of_parentheses):
        symbol: str = string_of_parentheses[index_position]

        if symbol == '(':
            nesting_level += 1
            temp_buffer.append(symbol)
        elif symbol == ')':
            nesting_level -= 1
            temp_buffer.append(symbol)
            if nesting_level == 0:
                grouped_results.append(''.join(temp_buffer))
                temp_buffer.clear()
        # else: no operation

        index_position += 1

    return grouped_results