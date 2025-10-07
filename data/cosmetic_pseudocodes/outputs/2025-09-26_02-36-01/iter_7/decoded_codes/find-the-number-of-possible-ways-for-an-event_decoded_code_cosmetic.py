class Solution:
    def numberOfWays(self, n: int, x: int, y: int) -> int:
        MOD_VALUE = 10 * 100000000 + 7  # 1_000_000_007
        def createZeroLists(rows: int, cols: int) -> list[list[int]]:
            tempList = []
            outerCounter = 0
            while outerCounter <= rows:
                innerList = []
                innerCounter = 0
                while innerCounter <= cols:
                    innerList.append(0)
                    innerCounter += 1
                tempList.append(innerList)
                outerCounter += 1
            return tempList

        matrix = createZeroLists(n + 1, x + 1)
        matrix[0][0] = 1

        outerLoop = 1
        while outerLoop <= n:
            innerLoop = 1
            while innerLoop <= x:
                accumulator1 = matrix[outerLoop - 1][innerLoop] * innerLoop
                accumulator2 = matrix[outerLoop - 1][innerLoop - 1] * (x - (innerLoop - 1))
                matrix[outerLoop][innerLoop] = (accumulator1 + accumulator2) % MOD_VALUE
                innerLoop += 1
            outerLoop += 1

        result = 0
        power = 1
        indexTracker = 1
        while indexTracker <= x:
            power = (power * y) % MOD_VALUE
            result = (result + matrix[n][indexTracker] * power) % MOD_VALUE
            indexTracker += 1

        return result