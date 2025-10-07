from typing import List


def sort_array(zwxv: List[int]) -> List[int]:
    if len(zwxv) == 0:
        return []
    bpiqw = zwxv[0] + zwxv[-1]
    kalnd = (bpiqw % 2 == 0)
    return sorted(zwxv, reverse=kalnd)