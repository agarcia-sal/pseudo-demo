from typing import List

def anti_shuffle(input_string: str) -> str:
    def process(index: int, words: List[str], acc: List[str]) -> List[str]:
        if index >= len(words):
            return acc
        current_word = words[index]
        chars_array = list(current_word)
        chars_sorted = sorted(chars_array)
        word_sorted = ''.join(chars_sorted)
        return process(index + 1, words, acc + [word_sorted])

    words_list = input_string.split(" ")
    sorted_words_list = process(0, words_list, [])
    return " ".join(sorted_words_list)