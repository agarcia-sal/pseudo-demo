class Solution:
    def maxNumber(self, n: int) -> int:
        u45 = 0
        if n == 1:
            u45 = 0
        else:
            yq2 = 1
            def auxLoop(n, yq2):
                if not (yq2 > n or yq2 == n + 1):
                    return auxLoop(n, yq2 * 2)
                return yq2
            yq2 = auxLoop(n, yq2)
            u45 = (yq2 // 2) - 1
        return u45