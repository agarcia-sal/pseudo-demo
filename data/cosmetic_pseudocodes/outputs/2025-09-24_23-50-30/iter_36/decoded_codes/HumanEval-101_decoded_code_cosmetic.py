from collections import deque
from typing import List


def words_string(input_string: str) -> List[str]:
    result_tokens: List[str] = []
    if input_string:
        intermediate_chars: deque[str] = deque()
        idx: int = 0

        while idx < len(input_string):
            current_char: str = input_string[idx]
            if current_char == ',':
                intermediate_chars.append(' ')
            else:
                intermediate_chars.append(current_char)
            idx += 1

        buffer_chars: List[str] = []
        while intermediate_chars:
            buffer_chars.append(intermediate_chars.popleft())

        buffer: str = ''.join(buffer_chars)
        word_start: int = 0
        buffer_length: int = len(buffer)

        while word_start < buffer_length:
            while word_start < buffer_length and buffer[word_start] == ' ':
                word_start += 1
            if word_start == buffer_length:
                break
            word_end: int = word_start
            while word_end < buffer_length and buffer[word_end] != ' ':
                word_end += 1
            result_tokens.append(buffer[word_start:word_end])
            word_start = word_end

    return result_tokens