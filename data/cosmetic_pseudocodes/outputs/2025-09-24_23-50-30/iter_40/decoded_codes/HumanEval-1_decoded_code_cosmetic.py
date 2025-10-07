from typing import List


def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    accumulator_results: List[str] = []
    collector_buffer: List[str] = []
    depth_level: int = 0
    index_pointer: int = 0

    while index_pointer < len(string_of_parentheses):
        symbol = string_of_parentheses[index_pointer]

        if symbol == '(':
            depth_level += 1
            collector_buffer.append(symbol)
        elif symbol == ')':
            depth_level -= 1
            collector_buffer.append(symbol)
            if depth_level == 0:
                accumulator_results.append("".join(collector_buffer))
                collector_buffer.clear()
        # NOOP for default case (ignore other characters)

        index_pointer += 1

    return accumulator_results