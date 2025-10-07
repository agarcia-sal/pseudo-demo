from typing import List

def select_words(string_s: str, natural_number_n: int) -> List[str]:
    output_list: List[str] = []
    words_collection: List[str] = string_s.split(" ")
    word_cursor: int = 0
    vowels = {"a", "e", "i", "o", "u"}
    while word_cursor < len(words_collection):
        curr_word = words_collection[word_cursor]
        consonant_count = 0
        idx = 0
        while idx < len(curr_word):
            curr_char = curr_word[idx].lower()
            if curr_char not in vowels:
                consonant_count += 1
            idx += 1
        if consonant_count == natural_number_n:
            output_list.append(curr_word)
        word_cursor += 1
    return output_list