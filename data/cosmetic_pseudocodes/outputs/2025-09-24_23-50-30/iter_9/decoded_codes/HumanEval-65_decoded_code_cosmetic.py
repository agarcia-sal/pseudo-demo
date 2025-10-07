def circular_shift(integer_alpha: int, integer_beta: int) -> str:
    string_omega: str = str(integer_alpha)
    if integer_beta >= len(string_omega):
        return string_omega[::-1]
    pivot: int = len(string_omega) - integer_beta
    left_part: str = string_omega[pivot:]
    right_part: str = string_omega[:pivot]
    return left_part + right_part