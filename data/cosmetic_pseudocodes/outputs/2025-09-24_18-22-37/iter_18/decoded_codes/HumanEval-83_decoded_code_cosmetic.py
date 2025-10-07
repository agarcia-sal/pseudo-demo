def starts_one_ends(qwerty: int) -> int:
    if qwerty == 1:
        return 1
    temp_var = qwerty - 2
    base_num = 10
    exponentiated_value = 1
    counter = 0
    while counter < temp_var:
        exponentiated_value *= base_num
        counter += 1
    return 18 * exponentiated_value