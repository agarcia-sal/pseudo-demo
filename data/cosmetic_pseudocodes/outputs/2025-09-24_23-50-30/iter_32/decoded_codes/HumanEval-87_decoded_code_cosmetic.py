from typing import List, Tuple

def get_row(matrix: List[List[int]], num: int) -> List[Tuple[int, int]]:
    list1: List[Tuple[int, int]] = []
    i: int = 0
    while i < len(matrix):
        j: int = 0
        while j < len(matrix[i]):
            if num == matrix[i][j]:
                temp: Tuple[int, int] = (i, j)
                list1.append(temp)
            j += 1
        i += 1

    list2: List[Tuple[int, int]] = []
    idx: int = 0
    while idx < len(list1):
        u = list1[idx]
        inserted = False
        k = 0
        while k < len(list2) and not inserted:
            if u[1] > list2[k][1]:
                list2.insert(k, u)
                inserted = True
            k += 1
        if not inserted:
            list2.append(u)
        idx += 1

    list3: List[Tuple[int, int]] = []
    m = 0
    while m < len(list2):
        val = list2[m]
        placed = False
        n = 0
        while n < len(list3) and not placed:
            if val[0] < list3[n][0]:
                list3.insert(n, val)
                placed = True
            n += 1
        if not placed:
            list3.append(val)
        m += 1
    return list3