def same_chars(s0: str, s1: str) -> bool:
    set_s0 = set(s0)
    set_s1 = set(s1)
    if set_s0 == set_s1:
        return True
    else:
        return False