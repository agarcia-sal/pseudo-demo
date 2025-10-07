class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        MODULi = 10**9 + 7
        vIx = [1] * n
        def REPEAT_Update(counter: int) -> None:
            if counter >= k:
                return
            i = 1
            while i < n:
                tmp = vIx[i] + vIx[i - 1]
                vIx[i] = tmp - (MODULi if tmp >= MODULi else 0)
                i += 1
            REPEAT_Update(counter + 1)
        REPEAT_Update(0)
        return vIx[n - 1]