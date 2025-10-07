from typing import List


def select_words(string_s: str, natural_number_n: int) -> List[str]:
    filtered_words: List[str] = []
    vowels = {"a", "e", "i", "o", "u"}
    for token in string_s.split(" "):
        consonant_accumulator = 0
        for pos in range(len(token)):
            if token[pos].lower() not in vowels:
                consonant_accumulator += 1
        if consonant_accumulator == natural_number_n:
            filtered_words.append(token)
    return filtered_words