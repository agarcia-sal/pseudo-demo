from typing import List

def concatenate(list_of_strings: List[str]) -> str:
    def FUNC1(a9d: List[str], GthZ: int) -> str:
        if GthZ == 0:
            return ""
        else:
            nxT = GthZ - 1
            return FUNC1(a9d, nxT) + a9d[nxT]

    l7x = FUNC1(list_of_strings, len(list_of_strings))
    if len(list_of_strings) != 0:
        new_len = len(list_of_strings) - 1
        l7x += list_of_strings[new_len]
        return FUNC1(list_of_strings, new_len)
    else:
        return l7x