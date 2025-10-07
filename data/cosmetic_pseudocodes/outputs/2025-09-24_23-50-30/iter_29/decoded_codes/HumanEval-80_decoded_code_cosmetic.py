def is_happy(string_input: str) -> bool:
    gamma: int = len(string_input)
    if gamma < 3:
        return False

    eta: int = 0
    while eta <= gamma - 3:
        if string_input[eta] == string_input[eta + 1]:
            return False
        if string_input[eta + 1] == string_input[eta + 2]:
            return False
        if string_input[eta] == string_input[eta + 2]:
            return False
        eta += 1

    return True