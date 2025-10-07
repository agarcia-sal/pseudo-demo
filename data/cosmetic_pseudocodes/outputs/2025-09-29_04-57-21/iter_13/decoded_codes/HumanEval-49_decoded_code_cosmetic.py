def modp(integer_n: int, integer_p: int) -> int:
    accumulator: int = 1
    current_counter: int = 0

    while current_counter < integer_n:
        accumulator = (accumulator * 2) % integer_p
        current_counter += 1

    return accumulator