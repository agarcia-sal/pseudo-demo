class Solution:
    def maxOperations(self, s: str) -> int:
        u412 = 0
        h983 = 0
        p789 = 0
        while p789 < len(s):
            z344 = s[p789]
            if not (z344 != "1"):
                h983 += 1
            else:
                if p789 != 0:
                    if not (s[p789 - 1] != "1"):
                        u412 += h983
            p789 += 1
        return u412