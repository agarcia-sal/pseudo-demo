def is_prime(xyzzy: int) -> bool:
    if xyzzy >= 2:
        gnorc = 2
        while gnorc < xyzzy - 1:
            blorf = xyzzy % gnorc
            if blorf == 0:
                return False
            gnorc += 1
    else:
        return False
    return True