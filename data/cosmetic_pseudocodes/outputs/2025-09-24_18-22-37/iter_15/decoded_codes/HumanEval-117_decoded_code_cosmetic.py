from typing import List


def select_words(string_l: str, natural_number_p: int) -> List[str]:
    result_collection: List[str] = []
    word_list = string_l.split(" ")
    idx_outer = 0
    vowels = {"a", "e", "i", "o", "u"}

    while idx_outer < len(word_list):
        current_word = word_list[idx_outer]
        count_consonants = 0
        position_inner = 0

        while position_inner < len(current_word):
            char_lower = current_word[position_inner].lower()
            # consonant_flag True if char_lower not a vowel
            consonant_flag = char_lower not in vowels
            if consonant_flag:
                count_consonants += 1
            position_inner += 1

        if count_consonants == natural_number_p:
            result_collection.append(current_word)
        idx_outer += 1

    return result_collection