from typing import List


def anti_shuffle(input_string: str) -> str:
    list_of_words: List[str] = input_string.split()
    ordered_words: List[str] = []
    for word in list_of_words:
        sorted_word: List[str] = sorted(word)
        ordered_words.append("".join(sorted_word))
    result_string: str = " ".join(ordered_words)
    return result_string