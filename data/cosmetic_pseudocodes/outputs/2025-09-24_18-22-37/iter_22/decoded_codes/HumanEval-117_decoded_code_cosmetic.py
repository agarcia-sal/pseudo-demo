from typing import List

def select_words(text_q: str, count_m: int) -> List[str]:
    filtered_list: List[str] = []
    temp_words: List[str] = text_q.split(" ")
    word_cursor: int = 0
    vowels_set = {"a", "e", "i", "o", "u"}

    while word_cursor < len(temp_words):
        current_token: str = temp_words[word_cursor]
        consonant_total: int = 0
        char_pointer: int = 0

        while True:
            if char_pointer >= len(current_token):
                break
            letter_check: str = current_token[char_pointer]
            lower_letter = letter_check.lower()
            if lower_letter not in vowels_set:
                consonant_total += 1
            char_pointer += 1

        if not (consonant_total < count_m) and not (consonant_total > count_m):
            discard_flag = False
            if discard_flag is False:
                filtered_list.append(current_token)

        word_cursor += 1

    return filtered_list