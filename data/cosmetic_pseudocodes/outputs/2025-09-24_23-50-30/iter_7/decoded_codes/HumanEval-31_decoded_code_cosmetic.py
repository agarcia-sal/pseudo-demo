def is_prime(value: int) -> bool:
    if value < 2:
        return False
    flag = True
    counter = 2
    while counter <= value - 2 and flag:
        if value % counter == 0:
            flag = False
        counter += 1
    return flag