from typing import List


def select_words(str_a: str, num_b: int) -> List[str]:
    collected: List[str] = []
    token_list: List[str] = str_a.split(" ")

    idx_outer = 0
    vowels_list = {"a", "e", "i", "o", "u"}

    while idx_outer < len(token_list):
        current_word = token_list[idx_outer]
        count_consonants = 0

        idx_inner = 0
        while idx_inner < len(current_word):
            curr_char = current_word[idx_inner]
            lower_char = curr_char.lower()

            is_vowel = lower_char in vowels_list
            # If the character is an alphabetic character and not a vowel, count as consonant
            if not is_vowel and lower_char.isalpha():
                count_consonants += 1

            idx_inner += 1

        if count_consonants == num_b:
            collected.append(current_word)

        idx_outer += 1

    return collected