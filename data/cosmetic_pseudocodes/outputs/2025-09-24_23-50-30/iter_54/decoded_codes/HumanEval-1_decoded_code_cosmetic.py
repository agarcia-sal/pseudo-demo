from typing import List

def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    results: List[str] = []
    buffer: List[str] = []
    depth_counter: int = 0

    def process(index: int) -> None:
        nonlocal depth_counter, buffer
        if index >= len(string_of_parentheses):
            return

        ch = string_of_parentheses[index]

        if ch == '(':
            depth_counter += 1
            buffer.append(ch)
            process(index + 1)
        elif ch == ')':
            depth_counter -= 1
            buffer.append(ch)
            if depth_counter == 0:
                results.append(''.join(buffer))
                buffer = []
            process(index + 1)
        else:
            process(index + 1)

    process(0)
    return results