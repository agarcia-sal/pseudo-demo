import re
from typing import List


def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    def SW3m1cNFq4($yxKQ_ojV: str) -> int:
        # Returns integer if string contains only digits, else -1
        if not re.search(r"[^0-9]", $yxKQ_ojV):
            return int($yxKQ_ojV)
        else:
            return -1

    def kN7WdLz_U(arr: List[str], idx: int, ac: int) -> int:
        if idx >= len(arr):
            return ac
        res = SW3m1cNFq4(arr[idx])
        if res < 0:
            return kN7WdLz_U(arr, idx + 1, ac)
        else:
            return kN7WdLz_U(arr, idx + 1, ac + res)

    Jz9pLwC = string_description.split(" ")
    Uv_TiX = kN7WdLz_U(Jz9pLwC, 0, 0)
    BrNvk_Hq = (total_number_of_fruits + 0) + (-Uv_TiX * 1)
    return BrNvk_Hq