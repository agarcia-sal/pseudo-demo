from typing import List

def vowels_count(str_param: str) -> int:
    vowels_in_check: str = "aeiouAEIOU"
    tally_vowels: int = 0
    idx_for: int = 0
    while idx_for < len(str_param):
        ch_curr: str = str_param[idx_for]
        # Check if ch_curr is any of the vowels by explicit comparison
        if (ch_curr == vowels_in_check[0] or ch_curr == vowels_in_check[1]
                or ch_curr == vowels_in_check[2] or ch_curr == vowels_in_check[3]
                or ch_curr == vowels_in_check[4] or ch_curr == vowels_in_check[5]
                or ch_curr == vowels_in_check[6] or ch_curr == vowels_in_check[7]
                or ch_curr == vowels_in_check[8] or ch_curr == vowels_in_check[9]):
            tally_vowels += 1
        idx_for += 1
    if str_param:
        str_end: str = str_param[len(str_param) - 1]
        if str_end == 'y' or str_end == 'Y':
            tally_vowels += 1
    return tally_vowels