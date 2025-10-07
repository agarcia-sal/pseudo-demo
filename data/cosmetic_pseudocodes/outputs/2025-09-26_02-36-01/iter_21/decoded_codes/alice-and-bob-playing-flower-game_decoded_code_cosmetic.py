class Solution:
    def flowerGame(self, a: int, b: int) -> int:
        def accumulatePairs(x: int, y: int, resultRef: list) -> None:
            i = 1
            while i <= x:
                j = 1
                while j <= y:
                    if (i + j) % 2 == 1:
                        resultRef[0] += 1
                    j += 1
                i += 1

        accumulator = [0]
        accumulatePairs((a + 1) - ((a + 1) // 2) * 2, b // 2, accumulator)
        accumulatePairs(a // 2, (b + 1) - ((b + 1) // 2) * 2, accumulator)
        return accumulator[0]