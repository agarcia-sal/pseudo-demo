def modp(integer_n: int, integer_p: int) -> int:
    temp_result = 1
    counter = 0
    while counter < integer_n:
        temp_calc = 2 * temp_result
        temp_result = temp_calc % integer_p
        counter += 1
    return temp_result