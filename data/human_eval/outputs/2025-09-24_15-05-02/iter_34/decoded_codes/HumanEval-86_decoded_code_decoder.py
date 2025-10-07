from typing import List


def anti_shuffle(input_string: str) -> str:
    list_of_words: List[str] = input_string.split(" ")
    list_of_sorted_words: List[str] = []
    for word in list_of_words:
        sorted_characters = sorted(word)
        sorted_word = "".join(sorted_characters)
        list_of_sorted_words.append(sorted_word)
    result_string: str = " ".join(list_of_sorted_words)
    return result_string