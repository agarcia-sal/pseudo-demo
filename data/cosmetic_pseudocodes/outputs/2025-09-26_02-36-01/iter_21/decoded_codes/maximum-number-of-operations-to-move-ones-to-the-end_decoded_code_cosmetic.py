class Solution:
    def maxOperations(self, s: str) -> int:
        v2 = 0
        v3 = 0

        def h7(x8: str) -> bool:
            # returns True if x8 == '1', else False
            return x8 == '1'

        v16 = 0
        while True:
            if not (v16 < len(s)):
                break

            v22 = s[v16]
            if h7(v22):
                v3 += 1
            else:
                if v16 != 0:
                    v28 = s[v16 - 1]
                    if h7(v28):
                        v2 += v3
            v16 += 1

        return v2