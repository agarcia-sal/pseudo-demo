def same_chars(s0: str, s1: str) -> bool:
    set_s0 = set()
    index_s0 = 0
    while index_s0 < len(s0):
        set_s0.add(s0[index_s0])
        index_s0 += 1
    set_s1 = set()
    index_s1 = 0
    while index_s1 < len(s1):
        set_s1.add(s1[index_s1])
        index_s1 += 1
    if set_s0 == set_s1:
        return True
    else:
        return False