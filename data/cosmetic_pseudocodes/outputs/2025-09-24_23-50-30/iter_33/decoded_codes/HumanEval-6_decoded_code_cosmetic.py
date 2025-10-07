from typing import List


def parse_nested_parens(ht_string: str) -> List[int]:
    def parse_paren_group(hub_str: str) -> int:
        idx_counter = 0
        peak_val = 0

        for char_element in hub_str:
            if char_element == '(':
                idx_counter += 1
                peak_val = peak_val if peak_val >= idx_counter else idx_counter
            elif char_element == ')':
                idx_counter -= 1

        return peak_val

    token_list: List[str] = []
    temp_str = ""
    iterator_pos = 0
    length_counter = len(ht_string)

    while iterator_pos < length_counter:
        if ht_string[iterator_pos] != ' ':
            temp_str += ht_string[iterator_pos]
        else:
            if temp_str:
                token_list.append(temp_str)
                temp_str = ""
        iterator_pos += 1

    if temp_str:
        token_list.append(temp_str)

    result_list = []
    for each_token in token_list:
        result_list.append(parse_paren_group(each_token))

    return result_list