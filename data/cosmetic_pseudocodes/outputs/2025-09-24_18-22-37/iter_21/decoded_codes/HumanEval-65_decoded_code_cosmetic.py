def circular_shift(param_a: object, param_b: int) -> str:
    temp_str = str(param_a)
    if param_b > len(temp_str):
        return temp_str[::-1]
    pivot = len(temp_str) - param_b
    return temp_str[pivot:] + temp_str[:pivot]