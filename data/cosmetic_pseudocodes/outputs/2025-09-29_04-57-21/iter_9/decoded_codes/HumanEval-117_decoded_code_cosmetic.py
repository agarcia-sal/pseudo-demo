from typing import List

def select_words(string_s: str, natural_number_n: int) -> List[str]:
    collected_words: List[str] = []
    word_iterator = iter(string_s.split(" "))
    vowels = {"a", "e", "i", "o", "u"}
    while True:
        try:
            current_word = next(word_iterator)
        except StopIteration:
            break
        consonant_tally = 0
        char_index = 0
        while char_index < len(current_word):
            current_char = current_word[char_index]
            if current_char.lower() not in vowels:
                consonant_tally += 1
            char_index += 1
        if consonant_tally == natural_number_n:
            collected_words.append(current_word)
    return collected_words