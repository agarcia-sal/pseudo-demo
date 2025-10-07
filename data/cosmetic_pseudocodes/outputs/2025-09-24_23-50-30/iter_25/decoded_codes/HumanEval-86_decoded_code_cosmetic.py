from typing import List


def anti_shuffle(input_string: str) -> str:
    temp_words: List[str] = input_string.split(" ")
    processed_words: List[str] = []
    idx: int = 0

    while idx < len(temp_words):
        current_word: str = temp_words[idx]
        chars: List[str] = list(current_word)
        ordered_chars: List[str] = sorted(chars)
        rebuilt_word: str = "".join(ordered_chars)
        processed_words.append(rebuilt_word)
        idx += 1

    return " ".join(processed_words)