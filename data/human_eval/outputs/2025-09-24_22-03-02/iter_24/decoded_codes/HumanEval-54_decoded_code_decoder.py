def same_chars(s0: str, s1: str) -> bool:
    set_s0 = ['']
    set_s1 = ['']
    for index in range(len(s0)):
        char_found = False
        for index2 in range(len(set_s0)):
            if set_s0[index2] == s0[index]:
                char_found = True
                break
        if not char_found:
            set_s0.append(s0[index])
    for index in range(len(s1)):
        char_found = False
        for index2 in range(len(set_s1)):
            if set_s1[index2] == s1[index]:
                char_found = True
                break
        if not char_found:
            set_s1.append(s1[index])
    if len(set_s0) != len(set_s1):
        return False
    for index in range(len(set_s0)):
        found_match = False
        for index2 in range(len(set_s1)):
            if set_s0[index] == set_s1[index2]:
                found_match = True
                break
        if not found_match:
            return False
    return True