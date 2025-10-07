def circular_shift(num_val: int, num_step: int) -> str:
    s_val = str(num_val)
    l_val = len(s_val)
    if num_step > l_val:
        return s_val[::-1]
    split_point = l_val - num_step
    return s_val[split_point:] + s_val[:split_point]