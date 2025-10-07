from typing import Dict

def get_closest_vowel(alphabet: str) -> str:
    if len(alphabet) < 3:
        return ""

    vowels_dict: Dict[str, bool] = {
        "a": True, "e": True, "i": True, "o": True, "u": True,
        "A": True, "E": True, "I": True, "O": True, "U": True
    }

    index_val: int = len(alphabet) - 2

    while index_val >= 1:
        ch_curr: str = alphabet[index_val]
        if vowels_dict.get(ch_curr, False):
            ch_next: str = alphabet[index_val + 1]
            ch_prev: str = alphabet[index_val - 1]

            if not vowels_dict.get(ch_next, False) and not vowels_dict.get(ch_prev, False):
                return ch_curr

        index_val -= 1

    return ""