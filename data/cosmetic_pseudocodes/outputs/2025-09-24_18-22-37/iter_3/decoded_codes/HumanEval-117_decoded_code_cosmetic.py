from typing import List

def select_words(string_s: str, natural_number_n: int) -> List[str]:
    result_collection: List[str] = []
    word_list: List[str] = []
    idx: int = 0
    length_s: int = len(string_s)
    while idx < length_s:
        current_word: str = ""
        while idx < length_s and string_s[idx] != ' ':
            current_word += string_s[idx]
            idx += 1
        if current_word:
            word_list.append(current_word)
        idx += 1  # Skip the space
    process_words(0, word_list, natural_number_n, result_collection)
    return result_collection

def process_words(pos: int, words_arr: List[str], target_count: int, acc: List[str]) -> None:
    if pos >= len(words_arr):
        return
    consonants: int = count_consonants(words_arr[pos], 0, 0)
    if consonants == target_count:
        acc.append(words_arr[pos])
    process_words(pos + 1, words_arr, target_count, acc)

def count_consonants(text: str, idx: int, count: int) -> int:
    if idx >= len(text):
        return count
    current_char: str = text[idx].lower()
    vowels = {"a", "e", "i", "o", "u"}
    delta: int = 0
    if current_char.isalpha() and current_char not in vowels:
        delta = 1
    return count_consonants(text, idx + 1, count + delta)