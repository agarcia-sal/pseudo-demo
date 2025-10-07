from collections import deque
from typing import List


def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    queue_segments: deque[str] = deque()
    buffer_chars: deque[str] = deque()
    depth_counter: int = 0

    def process_characters(index: int) -> None:
        nonlocal depth_counter
        if index >= len(string_of_parentheses):
            return

        current_char = string_of_parentheses[index]

        if current_char == '(':
            depth_counter += 1
            buffer_chars.append(current_char)
        elif current_char == ')':
            depth_counter -= 1
            buffer_chars.append(current_char)
            if depth_counter == 0:
                segment_string = ''.join(buffer_chars)
                queue_segments.append(segment_string)
                buffer_chars.clear()
        # Ignore other characters silently

        process_characters(index + 1)

    process_characters(0)

    result_list: List[str] = []
    while queue_segments:
        result_list.append(queue_segments.popleft())

    return result_list