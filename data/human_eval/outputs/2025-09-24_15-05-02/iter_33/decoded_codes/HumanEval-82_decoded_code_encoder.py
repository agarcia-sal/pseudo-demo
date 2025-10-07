def prime_length(input_string: str) -> bool:
    length_of_string: int = len(input_string)
    if length_of_string == 0 or length_of_string == 1:
        return False
    for i in range(2, length_of_string):
        if length_of_string % i == 0:
            return False
    return True