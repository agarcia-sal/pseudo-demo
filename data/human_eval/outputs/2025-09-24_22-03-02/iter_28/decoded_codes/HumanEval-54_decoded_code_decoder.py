def same_chars(s0: str, s1: str) -> bool:
    set_s0 = []
    index_s0 = 0
    while index_s0 < len(s0):
        char = s0[index_s0]
        found = False
        index_set_s0 = 0
        while index_set_s0 < len(set_s0) and not found:
            if char == set_s0[index_set_s0]:
                found = True
            index_set_s0 += 1
        if not found:
            set_s0.append(char)
        index_s0 += 1

    set_s1 = []
    index_s1 = 0
    while index_s1 < len(s1):
        char = s1[index_s1]
        found = False
        index_set_s1 = 0
        while index_set_s1 < len(set_s1) and not found:
            if char == set_s1[index_set_s1]:
                found = True
            index_set_s1 += 1
        if not found:
            set_s1.append(char)
        index_s1 += 1

    if len(set_s0) != len(set_s1):
        return False

    index_to_check = 0
    while index_to_check < len(set_s0):
        current_char = set_s0[index_to_check]
        found_in_s1 = False
        index_s1_check = 0
        while index_s1_check < len(set_s1) and not found_in_s1:
            if current_char == set_s1[index_s1_check]:
                found_in_s1 = True
            index_s1_check += 1
        if not found_in_s1:
            return False
        index_to_check += 1

    return True