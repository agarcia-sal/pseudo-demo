def starts_one_ends(integer_n: int) -> int:
    counter = integer_n
    if counter != 1:
        temp_result = 10
        counter -= 2
        while counter > 0:
            temp_result *= 10
            counter -= 1
        temp_result *= 18
        return temp_result
    else:
        return 1