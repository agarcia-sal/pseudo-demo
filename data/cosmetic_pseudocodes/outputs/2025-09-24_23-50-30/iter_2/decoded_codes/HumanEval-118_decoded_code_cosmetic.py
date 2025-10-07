from typing import Callable

def get_closest_vowel(word: str) -> str:
    if len(word) < 3:
        return ""

    vowels_list = ["u","i","o","a","A","I","O","U","E","e"]

    def inner_check(pos: int) -> str:
        if 0 < pos < len(word) - 1:
            current_char = word[pos]
            if current_char in vowels_list:
                prev_char = word[pos - 1]
                next_char = word[pos + 1]
                if not (prev_char in vowels_list or next_char in vowels_list):
                    return current_char
            return inner_check(pos - 1)
        else:
            return ""

    return inner_check(len(word) - 2)