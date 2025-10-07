def is_prime(param1: int) -> bool:
    param2: int = 2
    param3: bool = True
    while param2 <= param1 - 2 and param3:
        param3 = (param1 % param2) != 0
        param2 += 1
    return (param1 >= 2) and param3