def same_chars(s0: str, s1: str) -> bool:
    set_s0 = []
    set_s1 = []
    index = 0
    while index < len(s0):
        char = s0[index]
        found = False
        check_index = 0
        while check_index < len(set_s0):
            if set_s0[check_index] == char:
                found = True
                break
            check_index += 1
        if not found:
            set_s0.append(char)
        index += 1
    index = 0
    while index < len(s1):
        char = s1[index]
        found = False
        check_index = 0
        while check_index < len(set_s1):
            if set_s1[check_index] == char:
                found = True
                break
            check_index += 1
        if not found:
            set_s1.append(char)
        index += 1
    if len(set_s0) != len(set_s1):
        return False
    index = 0
    while index < len(set_s0):
        found = False
        check_index = 0
        while check_index < len(set_s1):
            if set_s0[index] == set_s1[check_index]:
                found = True
                break
            check_index += 1
        if not found:
            return False
        index += 1
    return True