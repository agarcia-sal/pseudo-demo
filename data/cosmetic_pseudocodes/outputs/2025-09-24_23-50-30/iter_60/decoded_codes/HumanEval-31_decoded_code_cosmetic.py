def is_prime(a: int) -> bool:
    def check_div(p: int) -> bool:
        if p > a - 2:
            return True
        elif a % p == 0:
            return False
        else:
            return check_div(p + 1)

    if a < 2:
        return False
    else:
        return check_div(2)