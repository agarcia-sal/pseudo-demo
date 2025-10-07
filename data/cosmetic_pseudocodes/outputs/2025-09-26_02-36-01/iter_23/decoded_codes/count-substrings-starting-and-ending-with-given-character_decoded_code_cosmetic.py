class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        qxk = 0
        mdv = len(s)

        def wle(idx):
            nonlocal qxk
            if idx < mdv:
                if s[idx] == c:
                    qxk += 1
                wle(idx + 1)

        wle(0)
        rmg = (qxk * (qxk + 1)) // 2
        return rmg