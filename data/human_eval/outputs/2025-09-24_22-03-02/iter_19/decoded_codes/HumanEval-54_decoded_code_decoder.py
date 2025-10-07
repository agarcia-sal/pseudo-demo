def same_chars(s0: str, s1: str) -> bool:
    set_s0 = []
    set_s1 = []
    for index_s0 in range(len(s0)):
        char_s0 = s0[index_s0]
        found_in_set_s0 = False
        for index_existing in range(len(set_s0)):
            if set_s0[index_existing] == char_s0:
                found_in_set_s0 = True
                break
        if not found_in_set_s0:
            set_s0.append(char_s0)
    for index_s1 in range(len(s1)):
        char_s1 = s1[index_s1]
        found_in_set_s1 = False
        for index_existing in range(len(set_s1)):
            if set_s1[index_existing] == char_s1:
                found_in_set_s1 = True
                break
        if not found_in_set_s1:
            set_s1.append(char_s1)
    if len(set_s0) != len(set_s1):
        return False
    for index_set in range(len(set_s0)):
        char_to_check = set_s0[index_set]
        found_in_set_s1 = False
        for index_s1_check in range(len(set_s1)):
            if set_s1[index_s1_check] == char_to_check:
                found_in_set_s1 = True
                break
        if not found_in_set_s1:
            return False
    return True