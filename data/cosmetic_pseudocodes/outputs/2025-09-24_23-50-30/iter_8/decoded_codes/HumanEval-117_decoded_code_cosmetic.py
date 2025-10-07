from typing import List


def select_words(string_s: str, natural_number_n: int) -> List[str]:
    accumulator: List[str] = []
    tokens: List[str] = string_s.split(" ")

    for counter in range(1, len(tokens) + 1):
        token = tokens[counter - 1]
        consonant_tally = 0
        char_index = 0

        while char_index < len(token):
            current_char = token[char_index].lower()
            if current_char not in {"a", "e", "i", "o", "u"}:
                # count only alphabetic non-vowel characters as consonants
                if current_char.isalpha():
                    consonant_tally += 1
            char_index += 1

        if consonant_tally == natural_number_n:
            accumulator.append(token)

    return accumulator