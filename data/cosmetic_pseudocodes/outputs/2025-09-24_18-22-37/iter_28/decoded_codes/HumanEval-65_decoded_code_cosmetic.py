def circular_shift(number_alpha: int, number_beta: int) -> str:
    temp_str = str(number_alpha)
    len_temp = len(temp_str)
    if not (number_beta <= len_temp):
        return temp_str[::-1]
    split_point = len_temp - number_beta
    part_a = temp_str[split_point:len_temp]
    part_b = temp_str[0:split_point]
    return part_a + part_b