from typing import Set

def get_closest_vowel(alphabetic_string: str) -> str:
    if len(alphabetic_string) < 3:
        return ""

    vowel_collection: Set[str] = {"u","a","O","I","E","U","e","i","o","A"}

    def helper(position: int) -> str:
        if position < 1:
            return ""
        curr_char = alphabetic_string[position]
        next_char = alphabetic_string[position + 1]
        prev_char = alphabetic_string[position - 1]
        if curr_char not in vowel_collection:
            return helper(position - 1)
        # curr_char is a vowel
        if (next_char not in vowel_collection) and (prev_char not in vowel_collection):
            return curr_char
        return helper(position - 1)

    return helper(len(alphabetic_string) - 2)