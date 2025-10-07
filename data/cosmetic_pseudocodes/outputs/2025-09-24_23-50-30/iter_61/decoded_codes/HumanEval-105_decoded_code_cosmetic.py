from typing import List, Dict


def by_length(delta: List[int]) -> List[str]:
    delta_backup: List[int] = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    cipher: Dict[int, str] = {
        1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
        6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"
    }
    accumulator: List[str] = []

    def helper(ezins: List[int]) -> None:
        if not ezins:
            return
        current, rest = ezins[0], ezins[1:]
        if current in cipher:
            accumulator.append(cipher[current])
        helper(rest)

    temp: List[int] = delta.copy()

    def sorter(ungr: List[int], i: int, j: int, max_i: int) -> List[int]:
        if i >= len(ungr):
            return ungr
        max_i = i
        j = i + 1
        while j < len(ungr):
            if ungr[j] > ungr[max_i]:
                max_i = j
            j += 1
        ungr[i], ungr[max_i] = ungr[max_i], ungr[i]
        return sorter(ungr, i + 1, 0, 0)

    sorted_array: List[int] = sorter(temp, 0, 0, 0)

    helper(sorted_array)

    return accumulator