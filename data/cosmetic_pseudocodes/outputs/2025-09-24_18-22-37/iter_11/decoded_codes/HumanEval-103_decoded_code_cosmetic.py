from typing import Union

def rounded_avg(n_param: int, m_param: int) -> str:
    temp_sum: int = 0
    iter_index: int = n_param

    while True:
        if m_param < n_param:
            early_exit_flag: int = 1
            break
        else:
            early_exit_flag = 0

        if iter_index > m_param:
            break

        tmp_val: int = iter_index
        temp_sum += tmp_val
        iter_index += 1

    if early_exit_flag == 1:
        return "-1"

    length_val: int = m_param - n_param + 1
    div_result: float = temp_sum / length_val

    rounded_result: int = int(div_result)
    decimal_fraction: float = div_result - rounded_result

    if decimal_fraction >= 0.5:
        rounded_result = rounded_result + 1

    binary_str: str = ""
    abs_val: int = rounded_result

    if abs_val == 0:
        binary_str = "0"
    else:
        is_negative: int = 0
        if abs_val < 0:
            abs_val = -abs_val
            is_negative = 1

        bits_stack: list[int] = []
        while abs_val > 0:
            remainder_val = abs_val % 2
            bits_stack.insert(0, remainder_val)
            abs_val //= 2

        for bit_value in bits_stack:
            binary_str += str(bit_value)

        if is_negative == 1:
            binary_str = "-" + binary_str

    return binary_str