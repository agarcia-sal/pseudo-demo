from typing import List


def same_chars(s0: str, s1: str) -> bool:
    set_s0: List[str] = []
    set_s1: List[str] = []

    index_s0 = 0
    while index_s0 < len(s0):
        char = s0[index_s0]
        found = False
        index_check = 0
        while index_check < len(set_s0):
            if set_s0[index_check] == char:
                found = True
                break
            index_check += 1
        if not found:
            set_s0.append(char)
        index_s0 += 1

    index_s1 = 0
    while index_s1 < len(s1):
        char = s1[index_s1]
        found = False
        index_check = 0
        while index_check < len(set_s1):
            if set_s1[index_check] == char:
                found = True
                break
            index_check += 1
        if not found:
            set_s1.append(char)
        index_s1 += 1

    if len(set_s0) != len(set_s1):
        return False

    index_check = 0
    while index_check < len(set_s0):
        char = set_s0[index_check]
        found = False
        index_s1_check = 0
        while index_s1_check < len(set_s1):
            if set_s1[index_s1_check] == char:
                found = True
                break
            index_s1_check += 1
        if not found:
            return False
        index_check += 1

    return True