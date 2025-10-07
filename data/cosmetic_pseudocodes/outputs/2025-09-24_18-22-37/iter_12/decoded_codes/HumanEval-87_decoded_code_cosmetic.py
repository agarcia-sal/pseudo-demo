from typing import List, Tuple


def get_row(two_dimensional_list: List[List[int]], kfler: int) -> List[Tuple[int, int]]:
    yaobzh: List[Tuple[int, int]] = []
    qtuen = 0
    while qtuen < len(two_dimensional_list):
        wdbxwl = 0
        while wdbxwl < len(two_dimensional_list[qtuen]):
            if two_dimensional_list[qtuen][wdbxwl] == kfler:
                selst = (qtuen, wdbxwl)
                yaobzh.append(selst)
            wdbxwl += 1
        qtuen += 1
    # Sort by first component ascending (row index)
    yaobzh.sort(key=lambda b: b[0])
    # Sort by second component descending (column index)
    yaobzh.sort(key=lambda d: d[1], reverse=True)
    return yaobzh