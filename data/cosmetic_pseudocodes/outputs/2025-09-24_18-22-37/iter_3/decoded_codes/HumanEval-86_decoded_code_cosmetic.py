from typing import List

def anti_shuffle(input_string: str) -> str:
    def sort_chars(word: str, index: int, chars_accum: List[str]) -> List[str]:
        if index >= len(word):
            return chars_accum
        current_char = word[index]
        return sort_chars(word, index + 1, chars_accum + [current_char])

    def sort_word(word: str) -> str:
        char_list = sort_chars(word, 0, [])
        sorted_list = sorted(char_list)
        return "".join(sorted_list)

    words_array = input_string.split(" ")

    def process_words(words: List[str], idx: int, acc: List[str]) -> List[str]:
        if idx == len(words):
            return acc
        sorted_version = sort_word(words[idx])
        return process_words(words, idx + 1, acc + [sorted_version])

    processed_list = process_words(words_array, 0, [])

    return " ".join(processed_list)