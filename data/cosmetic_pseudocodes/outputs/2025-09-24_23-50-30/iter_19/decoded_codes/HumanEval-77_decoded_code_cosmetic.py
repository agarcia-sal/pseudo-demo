def iscube(input_number: int) -> bool:
    reversed_sign_value = -input_number if input_number < 0 else input_number
    candidate_root = round(reversed_sign_value ** (1 / 3))
    return candidate_root ** 3 == reversed_sign_value