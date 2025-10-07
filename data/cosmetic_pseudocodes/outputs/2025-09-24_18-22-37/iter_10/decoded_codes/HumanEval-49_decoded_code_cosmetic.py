def modp(integer_n: int, integer_p: int) -> int:
    temp_accumulator: int = 1
    iterator_counter: int = 0
    while iterator_counter < integer_n:
        intermediate_calculation: int = 2 * temp_accumulator
        temp_accumulator = intermediate_calculation % integer_p
        iterator_counter += 1
    return temp_accumulator