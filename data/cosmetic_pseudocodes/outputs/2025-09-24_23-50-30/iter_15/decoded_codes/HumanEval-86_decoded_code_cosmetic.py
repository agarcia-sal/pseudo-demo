from collections import deque
from typing import Deque, List


def anti_shuffle(input_string: str) -> str:
    queue_of_tokens: Deque[str] = deque()
    index_marker: int = 0
    length: int = len(input_string)

    while index_marker < length:
        token_buffer = ""
        while index_marker < length and input_string[index_marker] != " ":
            token_buffer += input_string[index_marker]
            index_marker += 1
        queue_of_tokens.append(token_buffer)
        if index_marker < length and input_string[index_marker] == " ":
            index_marker += 1

    stack_of_sorted_words: List[str] = []

    while queue_of_tokens:
        current_token = queue_of_tokens.popleft()
        char_list: List[str] = [c for c in current_token]

        is_changed = True
        while is_changed:
            is_changed = False
            for i in range(len(char_list) - 1):
                if ord(char_list[i]) > ord(char_list[i + 1]):
                    char_list[i], char_list[i + 1] = char_list[i + 1], char_list[i]
                    is_changed = True

        rebuilt_word = "".join(char_list)
        stack_of_sorted_words.append(rebuilt_word)

    assembled_words: List[str] = []
    while stack_of_sorted_words:
        word_out = stack_of_sorted_words.pop()
        assembled_words.insert(0, word_out)

    output_string = " ".join(assembled_words)
    return output_string