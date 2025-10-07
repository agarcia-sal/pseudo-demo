from typing import List


def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    accumulator_kf: int = 0
    numeric_tokens_tq: List[int] = []
    tokens_vx: List[str] = string_description.split(" ")
    pointer_nz: int = 0
    while pointer_nz < len(tokens_vx):
        current_element_fg: str = tokens_vx[pointer_nz]
        pointer_nz += 1
        if "0" <= current_element_fg <= "9":  # string is a single digit character
            parsed_integer_hg: int = 0
            index_ru: int = 0
            length_element_os: int = len(current_element_fg)
            while index_ru < length_element_os:
                char_cf: str = current_element_fg[index_ru]
                digit_value_dw: int = ord(char_cf) - ord("0")
                parsed_integer_hg = (parsed_integer_hg * 10) + digit_value_dw
                index_ru += 1
            numeric_tokens_tq.append(parsed_integer_hg)
    count_sw: int = 0
    iterator_pl: int = 0
    while iterator_pl < len(numeric_tokens_tq):
        count_sw += numeric_tokens_tq[iterator_pl]
        iterator_pl += 1
    return total_number_of_fruits - count_sw