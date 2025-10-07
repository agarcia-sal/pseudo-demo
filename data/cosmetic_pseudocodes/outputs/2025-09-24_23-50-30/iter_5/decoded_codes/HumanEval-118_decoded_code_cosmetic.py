from typing import List

def get_closest_vowel(input_seq: List[str]) -> str:
    vowels_set = {"u", "e", "I", "A", "O", "o", "a", "E", "i", "U"}

    if len(input_seq) < 3:
        return ""

    def search_pos(position: int) -> str:
        if position < 1:
            return ""
        if (
            input_seq[position] in vowels_set
            and input_seq[position - 1] not in vowels_set
            and input_seq[position + 1] not in vowels_set
        ):
            return input_seq[position]
        return search_pos(position - 1)

    return search_pos(len(input_seq) - 2)