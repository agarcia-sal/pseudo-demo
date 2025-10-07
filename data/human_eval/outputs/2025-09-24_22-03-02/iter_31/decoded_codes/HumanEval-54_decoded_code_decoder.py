def same_chars(s0: str, s1: str) -> bool:
    set_s0 = set()
    set_s1 = set()
    index = 0
    while index < len(s0):
        set_s0.add(s0[index])
        index += 1
    index = 0
    while index < len(s1):
        set_s1.add(s1[index])
        index += 1
    return set_s0 == set_s1