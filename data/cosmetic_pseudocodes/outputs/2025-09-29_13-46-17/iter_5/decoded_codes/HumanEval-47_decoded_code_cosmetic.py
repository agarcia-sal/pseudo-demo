from typing import List, Union

def median(ArgList: List[Union[int, float]]) -> float:
    sortedList: List[Union[int, float]] = []

    def sortCopy(src: List[Union[int, float]], dest: List[Union[int, float]]) -> None:
        # Copy source list to destination list
        dest.extend(src)
        remaining = len(dest) - 1
        while remaining > 0:
            idx_outer = 0
            while idx_outer < remaining:
                if dest[idx_outer] > dest[idx_outer + 1]:
                    dest[idx_outer], dest[idx_outer + 1] = dest[idx_outer + 1], dest[idx_outer]
                idx_outer += 1
            remaining -= 1

    sortCopy(ArgList, sortedList)

    def medianHelper(lst: List[Union[int, float]], len_val: int) -> float:
        if (len_val % 2) != 0:
            return float(lst[(len_val - 1) // 2])
        first_mid = lst[(len_val // 2) - 1]
        second_mid = lst[len_val // 2]
        total = float(first_mid) + float(second_mid)
        return total / 2

    return medianHelper(sortedList, len(sortedList))