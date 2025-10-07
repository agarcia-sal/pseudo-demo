from typing import List


def minPath(grid: List[List[int]], k: int) -> List[int]:
    N: int = len(grid)
    V: int = (N * N) + 1
    oi: int = 0

    def processJ(oj: int, ok: int, acc_v: int) -> int:
        if oj == N:
            return acc_v

        _res_v: int = acc_v
        if grid[oi][oj] == 1:

            def gatherAdj(idx: int, arr: List[int]) -> List[int]:
                if idx == 4:
                    return arr
                _updated_arr = arr
                if idx == 0 and oi != 0:
                    _updated_arr = _updated_arr + [grid[oi - 1][oj]]
                if idx == 1 and oj != 0:
                    _updated_arr = _updated_arr + [grid[oi][oj - 1]]
                if idx == 2 and oi != (N - 1):
                    _updated_arr = _updated_arr + [grid[oi + 1][oj]]
                if idx == 3 and oj != (N - 1):
                    _updated_arr = _updated_arr + [grid[oi][oj + 1]]
                return gatherAdj(idx + 1, _updated_arr)

            collected = gatherAdj(0, [])
            min_val: int = collected[0]

            def minFind(pos: int, currentMin: int) -> int:
                if pos == len(collected):
                    return currentMin
                candidate = collected[pos]
                return minFind(pos + 1, candidate if candidate < currentMin else currentMin)

            _res_v = minFind(1, min_val)

        return processJ(oj + 1, ok, _res_v)

    def processI(ii: int, acc_val: int) -> int:
        nonlocal oi
        if ii == N:
            return acc_val
        oi = ii
        val_at_i = processJ(0, k, acc_val)
        return processI(ii + 1, val_at_i)

    val = processI(0, V)
    result: List[int] = []

    def fillAnswer(idx: int) -> None:
        if idx == k:
            return
        if idx % 2 == 0:
            result.append(1)
        else:
            result.append(val)
        fillAnswer(idx + 1)

    fillAnswer(0)
    return result