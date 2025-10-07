def same_chars(s0: str, s1: str):
    set_s0 = []
    set_s1 = []
    for i in range(len(s0)):
        if s0[i] not in set_s0:
            set_s0.append(s0[i])
    for j in range(len(s1)):
        if s1[j] not in set_s1:
            set_s1.append(s1[j])
    if len(set_s0) == len(set_s1):
        is_equal = True
        for k in range(len(set_s0)):
            found = False
            for m in range(len(set_s1)):
                if set_s0[k] == set_s1[m]:
                    found = True
                    break
            if not found:
                is_equal = False
                break
        return is_equal
    else:
        return False