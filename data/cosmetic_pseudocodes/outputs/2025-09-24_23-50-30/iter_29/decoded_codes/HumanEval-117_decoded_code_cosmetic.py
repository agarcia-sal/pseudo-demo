from typing import List


def select_words(string_s: str, natural_number_n: int) -> List[str]:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    accumulator: List[str] = []
    for token in string_s.split(" "):
        consonant_count = 0
        for position in range(len(token)):
            current_char = token[position].lower()
            if current_char not in vowels:
                consonant_count += 1
        if consonant_count == natural_number_n:
            accumulator.append(token)
    return accumulator