def circular_shift(param_a: object, param_b: int) -> str:
    temp_str: str = str(param_a)
    limit_val: int = len(temp_str)
    if param_b <= limit_val:
        split_index: int = limit_val - param_b
        first_part: str = temp_str[split_index:limit_val]
        second_part: str = temp_str[0:split_index]
        result_str: str = first_part + second_part
        return result_str
    else:
        return temp_str[::-1]