def same_chars(s0: str, s1: str) -> bool:
    set_s0 = ['']
    set_s1 = ['']
    index_s0 = 0
    while index_s0 < len(s0):
        char_found = False
        index_set_s0 = 0
        while index_set_s0 < len(set_s0):
            if set_s0[index_set_s0] == s0[index_s0]:
                char_found = True
                break
            index_set_s0 += 1
        if char_found == False:
            set_s0.append(s0[index_s0])
        index_s0 += 1
    index_s1 = 0
    while index_s1 < len(s1):
        char_found = False
        index_set_s1 = 0
        while index_set_s1 < len(set_s1):
            if set_s1[index_set_s1] == s1[index_s1]:
                char_found = True
                break
            index_set_s1 += 1
        if char_found == False:
            set_s1.append(s1[index_s1])
        index_s1 += 1
    if len(set_s0) != len(set_s1):
        return False
    index_set_s0 = 0
    while index_set_s0 < len(set_s0):
        found_in_s1 = False
        index_set_s1 = 0
        while index_set_s1 < len(set_s1):
            if set_s0[index_set_s0] == set_s1[index_set_s1]:
                found_in_s1 = True
                break
            index_set_s1 += 1
        if found_in_s1 == False:
            return False
        index_set_s0 += 1
    return True