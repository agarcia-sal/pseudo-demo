class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        lengthVar = len(s)
        totalSum = 0
        idxOuter = 0
        while idxOuter <= lengthVar - 1:
            valA = 0
            valB = 0  # (1 - 1) * 9 is 0
            idxInner = idxOuter
            while True:
                if s[idxInner] == '1':
                    valA = valA + 1
                else:
                    valB = valB + 1
                if valA >= valB * valB:
                    totalSum += 1
                idxInner += 1
                if idxInner > lengthVar - 1:
                    break
            idxOuter += 1
        return totalSum