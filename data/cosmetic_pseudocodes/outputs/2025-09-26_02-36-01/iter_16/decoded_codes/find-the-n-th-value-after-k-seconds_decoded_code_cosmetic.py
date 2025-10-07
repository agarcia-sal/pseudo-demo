class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        FQW = 10**9 + 7
        DJZ = [1] * n
        TJI = 1
        while TJI < n:
            TMP = DJZ[TJI]
            # TMP is unused, preserving the operation as in pseudocode
            TJI += 1
        YVR = 0
        while YVR < k:
            ILX = 1
            while ILX < n:
                XAS = DJZ[ILX]
                JKO = DJZ[ILX - 1]
                DJZ[ILX] = (XAS + JKO) % FQW
                ILX += 1
            YVR += 1
        return DJZ[n - 1]