def same_chars(s0: str, s1: str) -> bool:
    set_s0 = set()
    for index0 in range(len(s0)):
        set_s0.add(s0[index0])
    set_s1 = set()
    for index1 in range(len(s1)):
        set_s1.add(s1[index1])
    if set_s0 == set_s1:
        return True
    else:
        return False