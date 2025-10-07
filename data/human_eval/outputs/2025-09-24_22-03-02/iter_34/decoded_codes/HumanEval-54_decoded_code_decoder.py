def same_chars(s0, s1) -> bool:
    set_s0 = []
    set_s1 = []
    index = 0
    while index < len(s0):
        char_found = False
        inner_index = 0
        while inner_index < len(set_s0):
            if s0[index] == set_s0[inner_index]:
                char_found = True
                break
            inner_index += 1
        if not char_found:
            set_s0.append(s0[index])
        index += 1
    index = 0
    while index < len(s1):
        char_found = False
        inner_index = 0
        while inner_index < len(set_s1):
            if s1[index] == set_s1[inner_index]:
                char_found = True
                break
            inner_index += 1
        if not char_found:
            set_s1.append(s1[index])
        index += 1
    if len(set_s0) != len(set_s1):
        return False
    index = 0
    while index < len(set_s0):
        char_found = False
        inner_index = 0
        while inner_index < len(set_s1):
            if set_s0[index] == set_s1[inner_index]:
                char_found = True
                break
            inner_index += 1
        if not char_found:
            return False
        index += 1
    return True