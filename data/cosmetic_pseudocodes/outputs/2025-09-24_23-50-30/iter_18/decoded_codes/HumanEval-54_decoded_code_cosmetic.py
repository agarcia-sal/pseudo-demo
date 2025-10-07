from typing import Dict


def same_chars(string_p: str, string_q: str) -> bool:
    dictionary_p: Dict[str, bool] = {}
    dictionary_q: Dict[str, bool] = {}

    index_p = 0
    while index_p < len(string_p):
        dictionary_p[string_p[index_p]] = True
        index_p += 1

    index_q = 0
    while index_q < len(string_q):
        dictionary_q[string_q[index_q]] = True
        index_q += 1

    keys_p = []
    for key in dictionary_p:
        keys_p.append(key)

    keys_q = []
    for key in dictionary_q:
        keys_q.append(key)

    if len(keys_p) != len(keys_q):
        return False

    index_p = 0
    while index_p < len(keys_p):
        if keys_p[index_p] not in dictionary_q:
            return False
        index_p += 1

    return True