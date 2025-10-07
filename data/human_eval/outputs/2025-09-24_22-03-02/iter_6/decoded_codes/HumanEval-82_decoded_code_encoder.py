def prime_length(string) -> bool:
    length = len(string)
    if length == 0 or length == 1:
        return False
    for divisor in range(2, length):
        if length % divisor == 0:
            return False
    return True