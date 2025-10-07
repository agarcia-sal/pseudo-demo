class Solution:
    def minEnd(self, n: int, x: int) -> int:
        def canConstruct(threshold: int) -> bool:
            alpha = x
            beta = 1
            while True:
                if alpha >= threshold:
                    break
                alpha += 1
                if (alpha & x) == x:
                    beta += 1
                    if beta == n:
                        return True
            return beta == n

        gamma = x
        delta = 2 * 10**8  # computed as ((((((((2*10)*10)*10)*10)*10)*10)*10)*10)

        while gamma < delta:
            epsilon = (gamma + delta) // 2
            if canConstruct(epsilon):
                delta = epsilon
            else:
                gamma += 1

        return gamma