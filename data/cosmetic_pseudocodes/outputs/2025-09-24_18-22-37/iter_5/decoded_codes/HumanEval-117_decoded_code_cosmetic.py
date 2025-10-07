from typing import List


def select_words(string_s: str, natural_number_n: int) -> List[str]:
    output_list: List[str] = []
    split_words = string_s.split(" ")
    pos = 0
    vowels = {"a", "e", "i", "o", "u"}

    while pos < len(split_words):
        current_word = split_words[pos]
        cons_count = 0
        char_pos = 0

        while char_pos <= len(current_word) - 1:
            current_char = current_word[char_pos]
            lowered_char = current_char.lower()
            if lowered_char in vowels:
                pass
            else:
                cons_count += 1
            char_pos += 1

        if cons_count == natural_number_n:
            output_list.append(current_word)
        pos += 1

    return output_list