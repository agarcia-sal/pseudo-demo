from typing import Dict


def get_closest_vowel(term: str) -> str:
    if len(term) < 3:
        return ""

    nucleus: Dict[str, bool] = {symbol: True for symbol in ["a", "e", "i", "o", "u", "A", "E", "O", "U", "I"]}

    position = len(term) - 2
    while position >= 1:
        current_char = term[position]
        if current_char in nucleus:
            if term[position + 1] not in nucleus and term[position - 1] not in nucleus:
                return current_char
        position -= 1

    return ""