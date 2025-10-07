def same_chars(s0: str, s1: str) -> bool:
    set_s0 = []
    set_s1 = []
    for i in range(len(s0)):
        current_char = s0[i]
        found_in_set_s0 = False
        for j in range(len(set_s0)):
            if set_s0[j] == current_char:
                found_in_set_s0 = True
                break
        if not found_in_set_s0:
            set_s0.append(current_char)
    for i in range(len(s1)):
        current_char = s1[i]
        found_in_set_s1 = False
        for j in range(len(set_s1)):
            if set_s1[j] == current_char:
                found_in_set_s1 = True
                break
        if not found_in_set_s1:
            set_s1.append(current_char)
    if len(set_s0) != len(set_s1):
        return False
    for i in range(len(set_s0)):
        char_found_in_s1 = False
        for j in range(len(set_s1)):
            if set_s0[i] == set_s1[j]:
                char_found_in_s1 = True
                break
        if not char_found_in_s1:
            return False
    return True