def prime_length(input_string: str) -> bool:
    delta: int = len(input_string)
    if delta == 0 or delta == 1:
        return False
    iterator: int = 2
    while iterator < delta:
        if delta % iterator == 0:
            return False
        iterator += 1
    return True