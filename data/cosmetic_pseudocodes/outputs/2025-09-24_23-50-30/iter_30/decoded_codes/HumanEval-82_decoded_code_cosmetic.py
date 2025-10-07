def prime_length(input_string: str) -> bool:
    string_length: int = len(input_string)
    if string_length in (0, 1):
        return False

    counter: int = 2
    while counter < string_length:
        if string_length % counter != 0:
            counter += 1
        else:
            return False
    return True