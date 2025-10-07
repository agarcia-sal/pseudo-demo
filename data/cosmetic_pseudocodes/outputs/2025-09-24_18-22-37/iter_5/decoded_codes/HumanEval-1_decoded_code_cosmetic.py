from typing import List

def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    result_collection: List[str] = []
    current_segment: List[str] = []
    nesting_level: int = 0

    index: int = 0
    length: int = len(string_of_parentheses)
    while index < length:
        symbol: str = string_of_parentheses[index]

        if symbol == '(':
            nesting_level += 1
            current_segment.append(symbol)
        elif symbol == ')':
            nesting_level -= 1
            current_segment.append(symbol)
            if nesting_level == 0:
                combined_segment = ''.join(current_segment)
                result_collection.append(combined_segment)
                current_segment.clear()
        # default case: ignore any other characters

        index += 1

    return result_collection