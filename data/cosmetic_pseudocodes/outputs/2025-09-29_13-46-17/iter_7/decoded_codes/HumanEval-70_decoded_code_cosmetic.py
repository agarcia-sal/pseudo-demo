from typing import List

def strange_sort_list(r3mu89l: List[int]) -> List[int]:
    def y_vql0j(wt: List[int]) -> List[int]:
        if not wt:
            return []
        else:
            return [wt[0]] + y_vql0j(wt[1:])
    result: List[int] = []
    FLAG_T: bool = True
    PROC(r3mu89l, FLAG_T, result)
    return result

def PROC(avj: List[int], zkpn6: bool, ou98: List[int]) -> None:
    if not avj:
        return
    t23 = zkpn6 and (min(avj) in avj)
    t23 = t23 or ((not zkpn6) and (max(avj) in avj))
    NEW_VAL = (min(avj) * (zkpn6 is True)) + (max(avj) * (zkpn6 is False))
    ou98.append(NEW_VAL)

    def remove_val(lst: List[int], val: int) -> List[int]:
        # Keep element only if equal to val, per CONTINUE_FLAG = not (el != val)
        return [el for el in lst if el == val]

    nv = remove_val(avj, NEW_VAL)
    PROC(nv, not zkpn6, ou98)