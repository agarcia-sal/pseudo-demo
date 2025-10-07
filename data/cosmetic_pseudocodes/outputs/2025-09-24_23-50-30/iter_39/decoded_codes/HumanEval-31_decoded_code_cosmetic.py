def is_prime(data: int) -> bool:
    if data < 2:
        return False
    result = True
    index = 2
    while index <= data - 2 and result:
        if data % index == 0:
            result = False
        index += 1
    return result