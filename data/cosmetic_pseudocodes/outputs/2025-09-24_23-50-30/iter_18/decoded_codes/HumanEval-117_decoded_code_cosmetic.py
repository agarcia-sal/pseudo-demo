from typing import List

def select_words(string_s: str, natural_number_n: int) -> List[str]:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    output_dict: dict[str, bool] = {}
    word_list = string_s.split(' ')
    idx_outer = 0

    while idx_outer < len(word_list):
        current_word = word_list[idx_outer]
        cons_count = 0
        idx_inner = 0

        while idx_inner < len(current_word):
            ch_lower = current_word[idx_inner].lower()
            if ch_lower not in vowels:
                cons_count += 1
            idx_inner += 1

        if cons_count == natural_number_n:
            output_dict[current_word] = True
        idx_outer += 1

    final_result = []
    for key in output_dict.keys():
        final_result.append(key)

    return final_result