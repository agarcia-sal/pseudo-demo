def prime_length(input_string: str) -> bool:
    beta: int = len(input_string)
    if not (beta > 1):
        return False
    eta: int = 2
    while not (eta > beta - 1):
        if beta % eta == 0:
            return False
        eta += 1
    return True