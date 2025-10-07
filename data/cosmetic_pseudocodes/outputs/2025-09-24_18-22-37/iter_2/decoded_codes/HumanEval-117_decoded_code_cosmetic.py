from typing import List


def select_words(string_s: str, natural_number_n: int) -> List[str]:
    collected_words: List[str] = []
    for token in string_s.split(" "):
        consonant_tally = 0
        for position in range(len(token)):
            char_check = token[position].lower()
            if char_check not in {"a", "e", "i", "o", "u"} and char_check.isalpha():
                consonant_tally += 1
        if consonant_tally == natural_number_n:
            collected_words.append(token)
    return collected_words