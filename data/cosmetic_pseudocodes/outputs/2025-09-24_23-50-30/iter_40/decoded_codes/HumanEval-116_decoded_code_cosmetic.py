from typing import Iterable, List


def sort_array(seq: Iterable[int]) -> List[int]:
    def countOnes(x: int) -> int:
        return bin(x).count('1')

    interim_sorted = sorted(seq)
    result = sorted(interim_sorted, key=countOnes)
    return result