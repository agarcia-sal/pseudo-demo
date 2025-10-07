from typing import List

def select_words(string_s: str, natural_number_n: int) -> List[str]:
    vowels = "aeiou"
    result_list: List[str] = []
    words = string_s.split(" ")
    for idx in range(len(words)):
        current_word = words[idx]
        consonant_count = 0
        pos = 0
        while pos < len(current_word):
            letter = current_word[pos]
            letter_lower = letter.lower()
            if letter_lower not in vowels:
                consonant_count += 1
            pos += 1
        if consonant_count == natural_number_n:
            result_list.append(current_word)
    return result_list