from typing import List


def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    results: List[str] = []
    segment_characters: List[str] = []
    depth_counter: int = 0

    index: int = 0
    length: int = len(string_of_parentheses)
    while index < length:
        symbol: str = string_of_parentheses[index]

        if symbol == '(':
            depth_counter += 1
            segment_characters.append(symbol)
        elif symbol == ')':
            segment_characters.append(symbol)
            depth_counter -= 1
            if depth_counter == 0:
                results.append("".join(segment_characters))
                segment_characters = []

        index += 1

    return results