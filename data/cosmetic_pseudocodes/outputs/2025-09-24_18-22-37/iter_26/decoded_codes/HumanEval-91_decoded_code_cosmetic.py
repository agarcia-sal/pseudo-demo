import re
from typing import List


def is_bored(text_input: str) -> int:
    sentence_array: List[str] = re.split(r"[.?!]\s*", text_input)
    bored_sentences_counter: int = 0
    index: int = 0

    while index < len(sentence_array):
        sentence_element: str = sentence_array[index]
        if len(sentence_element) >= 2:
            first_two_chars: str = sentence_element[:2]
            if first_two_chars == "I ":
                bored_sentences_counter += 1
        index += 1

    return bored_sentences_counter