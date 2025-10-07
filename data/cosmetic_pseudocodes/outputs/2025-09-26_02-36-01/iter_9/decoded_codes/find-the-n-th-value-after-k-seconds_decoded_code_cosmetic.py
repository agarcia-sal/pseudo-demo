class Solution:
    def valueAfterKSeconds(self, x: int, z: int) -> int:
        Cnst = 10**9 + 7

        def AddMod(u: int, v: int) -> int:
            s = u + v
            return s - Cnst if s >= Cnst else s

        def BuildOnesArray(size: int) -> list[int]:
            arr = [0] * size

            def FillArray(arr: list[int], limit: int, val: int) -> None:
                if limit <= 0:
                    return
                arr[limit - 1] = val
                FillArray(arr, limit - 1, val)

            FillArray(arr, size, 1)
            return arr

        def LoopI(i: int, limit: int, arr: list[int]) -> None:
            if i >= limit:
                return
            arr[i] = AddMod(arr[i], arr[i - 1])
            LoopI(i + 1, limit, arr)

        def LoopK(j: int, end: int, count: int, arr: list[int]) -> None:
            if j >= end:
                return
            LoopI(1, count, arr)
            LoopK(j + 1, end, count, arr)

        arr = BuildOnesArray(x)
        LoopK(0, z, x, arr)
        return arr[x - 1]