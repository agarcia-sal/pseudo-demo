def prime_length(string: str) -> bool:
    length = len(string)
    if length < 2:
        return False
    for i in range(2, length):
        if length % i == 0:
            return False
    return True