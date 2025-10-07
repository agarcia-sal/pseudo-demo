from typing import List


def fruit_distribution(description_string: str, fruit_count_total: int) -> int:
    accumulated_values: List[int] = []
    temp_str_list = description_string.split(" ")
    idx = 0
    while True:
        if idx >= len(temp_str_list):
            break
        current_token = temp_str_list[idx]
        idx += 1
        is_digit_flag = True
        for c in current_token:
            if c < '0' or c > '9':
                is_digit_flag = False
                break
        if is_digit_flag:
            parsed_num = 0
            for ch in current_token:
                parsed_num = parsed_num * 10 + (ord(ch) - ord('0'))
            accumulated_values.append(parsed_num)
    total_accumulated = 0
    for i in range(len(accumulated_values)):
        total_accumulated += accumulated_values[i]
    result_output = fruit_count_total + (-1 * total_accumulated)
    return result_output