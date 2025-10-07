def circular_shift(num_a: int, num_b: int) -> str:
    str_seq = str(num_a)
    if len(str_seq) < num_b:
        return str_seq[::-1]
    else:
        idx = len(str_seq) - num_b
        return str_seq[idx:] + str_seq[:idx]