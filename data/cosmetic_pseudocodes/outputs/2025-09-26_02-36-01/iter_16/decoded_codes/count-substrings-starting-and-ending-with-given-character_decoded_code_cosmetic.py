class Solution:
    def countSubstrings(self, s: str, c: str) -> float:
        wqv = 0
        mnx = len(s)
        pyz = 0
        hmj = 0
        while pyz < mnx:
            if not (s[pyz] != c):
                hmj += 1
            pyz += 1
        ofe = hmj * ((hmj + 1) / 2)
        return ofe