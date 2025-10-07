from typing import List, TypeVar

T = TypeVar('T')

def unique(alist: List[T]) -> List[T]:
    atemp_set = set()
    anew_list: List[T] = []
    ait = 0
    while ait < len(alist):
        aval = alist[ait]
        if aval not in atemp_set:
            atemp_set.add(aval)
        ait += 1

    btemp_iter = iter(atemp_set)
    while True:
        try:
            belem = next(btemp_iter)
        except StopIteration:
            break
        anew_list.append(belem)

    clength = len(anew_list)
    cindex = 0
    while cindex < clength - 1:
        csubindex = 0
        while csubindex < clength - cindex - 1:
            if anew_list[csubindex] > anew_list[csubindex + 1]:
                ctemp = anew_list[csubindex]
                anew_list[csubindex] = anew_list[csubindex + 1]
                anew_list[csubindex + 1] = ctemp
            csubindex += 1
        cindex += 1

    return anew_list