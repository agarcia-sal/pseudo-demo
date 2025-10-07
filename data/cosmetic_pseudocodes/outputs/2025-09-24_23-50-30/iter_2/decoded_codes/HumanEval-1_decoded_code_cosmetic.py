from collections import deque
from typing import List

def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    results: deque[str] = deque()
    buffer: list[str] = []
    depth_counter: int = 0

    def process_chars(index: int) -> None:
        nonlocal depth_counter
        if index >= len(string_of_parentheses):
            return

        char = string_of_parentheses[index]
        if char != '(' and char != ')':
            process_chars(index + 1)
            return

        buffer.append(char)
        if char == '(':
            depth_counter += 1
        else:
            depth_counter -= 1
            if depth_counter == 0:
                temp = ''
                while buffer:
                    temp = buffer.pop() + temp
                results.append(temp)

        process_chars(index + 1)

    process_chars(0)

    output_list: List[str] = []
    while results:
        output_list.append(results.popleft())

    return output_list