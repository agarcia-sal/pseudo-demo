from typing import List


def words_string(original_text: str) -> List[str]:
    if not original_text:
        return []

    temp_chars: List[str] = []
    idx: int = 0
    while idx < len(original_text):
        current_char = original_text[idx]
        if current_char == ",":
            temp_chars.append(" ")
        else:
            temp_chars.append(current_char)
        idx += 1

    combined_str = ""
    letter_pos: int = 0
    while letter_pos < len(temp_chars):
        combined_str += temp_chars[letter_pos]
        letter_pos += 1

    split_words: List[str] = []
    word_start: int = 0
    word_end: int = 0
    combined_length: int = len(combined_str)
    while word_end <= combined_length:
        if word_end == combined_length or combined_str[word_end] == " ":
            if word_end > word_start:
                split_words.append(combined_str[word_start:word_end])
            word_start = word_end + 1
        word_end += 1

    return split_words