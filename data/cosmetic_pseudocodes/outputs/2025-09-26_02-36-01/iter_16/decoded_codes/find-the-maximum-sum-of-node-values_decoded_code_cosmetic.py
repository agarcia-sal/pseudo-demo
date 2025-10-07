class Solution:
    def maximumValueSum(self, nums, k):
        XrJqz = 0
        AjBsn = 0
        uNEXF = float('inf')

        for LdvJo in nums:
            YTnhR = LdvJo ^ k
            clNeu = YTnhR - LdvJo
            if clNeu > 0:
                AjBsn += 1
            XrJqz += LdvJo if LdvJo >= YTnhR else YTnhR
            abs_clNeu = -clNeu if clNeu < 0 else clNeu
            if uNEXF > abs_clNeu:
                uNEXF = abs_clNeu

        if AjBsn % 2 != 0:
            XrJqz -= uNEXF

        return XrJqz