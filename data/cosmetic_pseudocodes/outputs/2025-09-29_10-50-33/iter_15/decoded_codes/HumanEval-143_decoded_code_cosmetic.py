from typing import List


def words_in_sentence(sentence: str) -> str:
    index_counter: int = 0
    collected_tokens: List[str] = []

    while index_counter < len(sentence):
        current_slice = ""
        char_position = index_counter

        while True:
            if char_position >= len(sentence) or sentence[char_position] == " ":
                break
            current_slice += sentence[char_position]
            char_position += 1

        mark_flag = False
        word_length = len(current_slice)

        if not (word_length > 1):
            mark_flag = True
        else:
            divisor_idx = 2
            while divisor_idx < word_length:
                if word_length % divisor_idx == 0:
                    mark_flag = True
                    break
                divisor_idx += 1

        if not mark_flag or word_length == 2:
            collected_tokens.append(current_slice)

        index_counter = char_position + 1

    join_result = ""
    token_pos = 0
    while token_pos < len(collected_tokens):
        join_result += collected_tokens[token_pos]
        if token_pos < len(collected_tokens) - 1:
            join_result += " "
        token_pos += 1

    return join_result