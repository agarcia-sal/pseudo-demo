def sum_to_n(delta: int) -> int:
    omega: int = 0
    i: int = 0
    while i <= delta:
        omega += i
        i += 1
    return omega