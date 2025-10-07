from typing import List, Dict


def is_sorted(list_of_numbers: List[int]) -> bool:
    def mapKeysToZeros(lst: List[int]) -> Dict[int, int]:
        counts: Dict[int, int] = {}

        def helper(n: int) -> Dict[int, int]:
            if n == 0:
                return counts
            else:
                key = lst[len(lst) - n]
                counts[key] = 0
                return helper(n - 1)

        return helper(len(lst))

    counts_map = mapKeysToZeros(list_of_numbers)
    arr = list_of_numbers

    def count_occurrences(m: Dict[int, int], i: int) -> Dict[int, int]:
        if i == len(arr):
            return m
        else:
            key = arr[i]
            m[key] += 1
            return count_occurrences(m, i + 1)

    counts_map = count_occurrences(counts_map, 0)

    def hasMoreThanTwo(d: Dict[int, int]) -> bool:
        keys_list = list(d.keys())

        def check(idx: int) -> bool:
            if idx == len(keys_list):
                return False
            elif d[keys_list[idx]] > 2:
                return True
            else:
                return check(idx + 1)

        return check(0)

    if hasMoreThanTwo(counts_map):
        return False

    def allNonDecreasing(start: int) -> bool:
        def aux(pos: int) -> bool:
            if pos >= len(arr) - 1:
                return True
            if not (arr[pos - 1] <= arr[pos]):
                return False
            return aux(pos + 1)

        return aux(start)

    return allNonDecreasing(1)