from typing import List


def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    results: List[str] = []
    accumulator: List[str] = []
    depth_counter: int = 0

    for symbol in string_of_parentheses:
        if symbol == '(':
            depth_counter += 1
            accumulator.append(symbol)
        elif symbol == ')':
            depth_counter -= 1
            accumulator.append(symbol)
            if depth_counter == 0:
                results.append(''.join(accumulator))
                accumulator = []

    return results