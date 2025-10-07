from typing import List

def same_chars(str_a: str, str_b: str) -> bool:
    list_p: List[str] = []
    list_q: List[str] = []
    for idx_x in range(len(str_a)):
        if str_a[idx_x] not in list_p:
            list_p.append(str_a[idx_x])
    for idx_x in range(len(str_b)):
        if str_b[idx_x] not in list_q:
            list_q.append(str_b[idx_x])
    for idx_x in range(len(list_p)):
        if list_p[idx_x] not in list_q:
            return False
    for idx_x in range(len(list_q)):
        if list_q[idx_x] not in list_p:
            return False
    return True