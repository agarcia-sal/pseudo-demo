from typing import List


def select_words(string_s: str, natural_number_n: int) -> List[str]:
    result: List[str] = []
    words = string_s.split(" ")
    i = 0
    while i < len(words):
        current_word = words[i]
        p_count = 0
        j = 0
        while j < len(current_word):
            ch = current_word[j].lower()
            consonant_check = ch not in {"a", "e", "i", "o", "u"}
            if consonant_check:
                p_count += 1
            j += 1
        if p_count == natural_number_n:
            result.append(current_word)
        i += 1
    return result