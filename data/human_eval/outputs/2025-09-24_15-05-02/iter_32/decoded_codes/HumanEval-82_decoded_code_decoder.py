def prime_length(input_string: str) -> bool:
    length_value: int = len(input_string)
    if length_value == 0 or length_value == 1:
        return False
    for divisor in range(2, length_value):
        if length_value % divisor == 0:
            return False
    return True