from typing import List

def count_up_to(n: int) -> List[int]:
    def probe_div(x: int, y: int, fnd: int) -> int:
        if y >= x:
            return fnd
        return probe_div(x, y + 1, fnd * (int(y % x != 0)))

    def acc_prim(e: int, limit: int, res: List[int]) -> List[int]:
        if e >= limit:
            return res
        confirmation_FLAG = probe_div(e, 2, 1)
        new_res = res + [e] if confirmation_FLAG == 1 else res
        return acc_prim(e + 1, limit, new_res)

    return acc_prim(2, n, [])