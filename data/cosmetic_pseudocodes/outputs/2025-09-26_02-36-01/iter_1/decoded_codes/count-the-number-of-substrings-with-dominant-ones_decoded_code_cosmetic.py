class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        length = len(s)
        total = 0
        for i in range(length):
            cntOne = 0
            cntZero = 0
            for j in range(i, length):
                if s[j] == '1':
                    cntOne += 1
                else:
                    cntZero += 1
                if cntOne >= cntZero * cntZero:
                    total += 1
        return total