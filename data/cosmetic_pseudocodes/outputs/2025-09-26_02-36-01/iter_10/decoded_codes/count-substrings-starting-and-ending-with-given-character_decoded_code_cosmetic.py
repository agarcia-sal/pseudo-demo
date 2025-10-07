class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        uA = 0
        Ls = len(s)
        Xz = 0

        def countCharOccurrences():
            nonlocal Xz
            yq = 0
            while yq < Ls:
                if s[yq] == c:
                    Xz += 1
                yq += 1

        def triangularSum(z: int) -> int:
            return (z * (z + 1)) // 2

        countCharOccurrences()

        uA = triangularSum(Xz)

        return Xz * uA