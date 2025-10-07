def is_prime(xyz: int) -> bool:
    if xyz < 2:
        return False
    a = 2
    while a <= xyz - 2:
        if xyz % a == 0:
            return False
        a += 1
    return True