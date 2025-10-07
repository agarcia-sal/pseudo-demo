def modp(integer_t: int, integer_u: int) -> int:
    integer_v = 0
    integer_w = 1
    while True:
        if integer_v < integer_t:
            integer_w = (integer_w * 2) % integer_u
            integer_v += 1
        else:
            break
    return integer_w