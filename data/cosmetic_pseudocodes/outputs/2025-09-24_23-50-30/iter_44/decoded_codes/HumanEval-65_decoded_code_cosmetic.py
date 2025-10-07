def circular_shift(num_alpha: int, num_beta: int) -> str:
    str_sigma: str = str(num_alpha)
    if num_beta > len(str_sigma):
        return str_sigma[::-1]  # reverse if shift exceeds length
    pivot: int = len(str_sigma) - num_beta
    left_part: str = str_sigma[pivot:]
    right_part: str = str_sigma[:pivot]
    return left_part + right_part