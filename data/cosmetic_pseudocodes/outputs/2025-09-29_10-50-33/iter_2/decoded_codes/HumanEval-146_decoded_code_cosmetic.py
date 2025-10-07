from typing import List

def specialFilter(list_of_numbers: List[int]) -> int:
    total_matches: int = 0
    odd_set = {1, 3, 5, 7, 9}
    for candidate in list_of_numbers:
        if candidate > 10:
            text_form = str(candidate)
            first_char_num = int(text_form[0])
            last_char_num = int(text_form[-1])
            if first_char_num in odd_set and last_char_num in odd_set:
                total_matches += 1
    return total_matches