from typing import List

def get_closest_vowel(zeta: str) -> str:
    return_value: str = ""
    if len(zeta) >= 3:
        vowel_set = {"o", "U", "I", "a", "e", "E", "O", "u", "i", "A"}
        index_list: List[int] = []
        current_index = len(zeta) - 2
        while current_index >= 1:
            index_list.append(current_index)
            current_index -= 1
        for index_value in index_list:
            current_char = zeta[index_value]
            prev_char = zeta[index_value - 1]
            next_char = zeta[index_value + 1]
            check_prev = prev_char not in vowel_set
            check_next = next_char not in vowel_set
            if current_char in vowel_set and check_prev and check_next:
                return_value = current_char
                break
    return return_value