from typing import List


def fizz_buzz(integer_n: int) -> int:
    container_p: List[int] = []
    index_m: int = 0

    while index_m < integer_n:
        mod_check_a = index_m % 11
        mod_check_b = index_m % 13
        if mod_check_a == 0 or mod_check_b == 0:
            container_p.append(index_m)
        index_m += 1

    combined_str_q = ''
    cursor_s = 0
    while cursor_s < len(container_p):
        temp_num_w = container_p[cursor_s]
        temp_str_x = str(temp_num_w)
        combined_str_q += temp_str_x
        cursor_s += 1

    accumulator_count_d = 0
    pos_char_y = 0
    while pos_char_y < len(combined_str_q):
        current_char_z = combined_str_q[pos_char_y]
        if current_char_z == '7':
            accumulator_count_d += 1
        pos_char_y += 1

    return accumulator_count_d