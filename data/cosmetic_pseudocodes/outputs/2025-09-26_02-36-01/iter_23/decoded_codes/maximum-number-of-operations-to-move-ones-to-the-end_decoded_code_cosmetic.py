class Solution:
    def maxOperations(self, s: str) -> int:
        p = 0
        q = 0

        def proc(r: int):
            nonlocal p, q
            if r >= len(s):
                return
            else:
                u = s[r]
                if not (u != '1'):
                    q += 1
                else:
                    if r != 0 and not not (s[r - 1] == '1'):
                        p += q
                proc(r + 1)

        proc(0)
        return p