from typing import List

class Solution:
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        def is_peak(x: int) -> bool:
            def smaller(a: int, b: int) -> bool:
                return a < b

            def larger(a: int, b: int) -> bool:
                return a > b

            return smaller(nums[x - 1], nums[x]) and larger(nums[x], nums[x + 1])

        def bisect_left(arr: List[int], val: int) -> int:
            p, q = 0, len(arr)
            while p < q:
                m = (p + q) // 2
                if arr[m] < val:
                    p = m + 1
                else:
                    q = m
            return p

        def bisect_right(arr: List[int], val: int) -> int:
            p, q = 0, len(arr)
            while p < q:
                m = (p + q) // 2
                if val < arr[m]:
                    q = m
                else:
                    p = m + 1
            return p

        A = []
        n = len(nums)

        for H in range(1, n - 1):
            if is_peak(H):
                A.append(H)

        ret = []

        def insert_into_sorted(LISTQ: List[int], VALUEQ: int) -> None:
            posq = bisect_left(LISTQ, VALUEQ)
            LISTQ.insert(posq, VALUEQ)

        def remove_from_sorted(LISTR: List[int], VALUER: int) -> None:
            leftR = bisect_left(LISTR, VALUER)
            if leftR < len(LISTR) and LISTR[leftR] == VALUER:
                del LISTR[leftR]

        for qE in queries:
            if qE[0] == 1:
                LQ, RQ = qE[1], qE[2]
                liq = bisect_left(A, LQ + 1)
                riq = bisect_right(A, RQ) - 1
                diffq = riq - liq
                ret.append(diffq)
            else:
                idxq, valq = qE[1], qE[2]
                if nums[idxq] == valq:
                    continue
                nums[idxq] = valq
                start_pos = max(1, idxq - 1)
                end_pos = min(n - 2, idxq + 1)

                w = start_pos
                while w <= end_pos:
                    ip = w
                    if is_peak(ip):
                        if bisect_left(A, ip) == bisect_right(A, ip):
                            insert_into_sorted(A, ip)
                    else:
                        remove_from_sorted(A, ip)
                    w += 1

        return ret