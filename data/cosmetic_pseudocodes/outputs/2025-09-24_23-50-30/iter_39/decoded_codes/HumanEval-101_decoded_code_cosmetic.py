from typing import List


def words_string(foo: str) -> List[str]:
    if foo == "":
        return []

    cache: List[str] = []

    i = 0
    while i < len(foo):
        sym = foo[i]
        if sym == ',':
            cache.append(" ")
        else:
            cache.append(sym)
        i += 1

    res = "".join(cache)

    return res.split()