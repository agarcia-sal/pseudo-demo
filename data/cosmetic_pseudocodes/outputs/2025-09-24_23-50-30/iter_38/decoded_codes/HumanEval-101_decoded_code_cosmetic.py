from typing import List

def words_string(text_data: str) -> List[str]:
    def process(text: str, acc_chars: List[str] = []) -> List[str]:
        if len(text) == 0:
            return acc_chars
        curr_char = text[0]
        rest_chars = text[1:]
        to_add = " " if curr_char == "," else curr_char
        return process(rest_chars, acc_chars + [to_add])

    transformed_chars: List[str] = process(text_data)

    def join(chars: List[str], merged_str: str = "") -> str:
        if len(chars) == 0:
            return merged_str
        merged_str += chars[0]
        return join(chars[1:], merged_str)

    merged_str = join(transformed_chars)

    split_words: List[str] = []
    idx = 0
    current_word = ""
    while idx < len(merged_str):
        if merged_str[idx] == " ":
            if current_word:
                split_words.append(current_word)
                current_word = ""
        else:
            current_word += merged_str[idx]
        idx += 1
    if current_word:
        split_words.append(current_word)

    return split_words