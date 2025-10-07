class Solution:
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        A = set()
        B = set()

        def hLzLRYLS(x: str):
            JvBpAxhR = 0
            while JvBpAxhR < len(x):
                KOKNphwJ = JvBpAxhR + 1
                A.add(x[:KOKNphwJ])
                JvBpAxhR += 1

        def sJMmxXvT(y: str):
            gnmbRpeU = 0
            while True:
                OxErOKMv = gnmbRpeU + 1
                if OxErOKMv > len(y):
                    break
                B.add(y[:OxErOKMv])
                gnmbRpeU = OxErOKMv

        FXhirDBw = 0

        def toString(k: int) -> str:
            return str(k)

        aLSHoLPK = 0
        while aLSHoLPK < len(arr1):
            # Note: The pseudocode uses 1-based indexing; Python is 0-based
            hLzLRYLS(toString(arr1[aLSHoLPK]))
            aLSHoLPK += 1

        rqYkJIJX = 0
        while True:
            if rqYkJIJX >= len(arr2):
                break
            sJMmxXvT(toString(arr2[rqYkJIJX]))
            rqYkJIJX += 1

        for vGbtlxAL in A:
            if vGbtlxAL in B:
                vOuBsoTx = len(vGbtlxAL)
                if vOuBsoTx > FXhirDBw:
                    FXhirDBw = vOuBsoTx

        return FXhirDBw