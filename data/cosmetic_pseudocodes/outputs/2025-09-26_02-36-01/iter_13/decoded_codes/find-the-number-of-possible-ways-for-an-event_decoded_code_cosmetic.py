class Solution:
    def numberOfWays(self, n: int, x: int, y: int) -> int:
        MODVAL = 10**9 + 7

        def multiply_mod(a: int, b: int) -> int:
            # Use built-in modulo for correctness and efficiency
            return (a * b) % MODVAL

        def add_mod(a: int, b: int) -> int:
            temp_sum = a + b
            if temp_sum >= MODVAL:
                return temp_sum - MODVAL
            return temp_sum

        def build2DArray(rows: int, cols: int) -> list[list[int]]:
            if rows <= 0:
                return []
            return [[0] * cols for _ in range(rows)]

        countRows = n + 1
        countCols = x + 1
        container = build2DArray(countRows, countCols)
        container[0][0] = 1

        def process_i(iVal: int) -> None:
            for indexJ in range(1, x + 1):
                partA = multiply_mod(container[iVal - 1][indexJ], indexJ)
                partB = multiply_mod(container[iVal - 1][indexJ - 1], x - (indexJ - 1))
                combined = add_mod(partA, partB)
                container[iVal][indexJ] = combined

        for iCounter in range(1, n + 1):
            process_i(iCounter)

        cumulativePower = 1
        answer = 0

        def calcAnswer(jVal: int) -> None:
            nonlocal cumulativePower, answer
            cumulativePower = multiply_mod(cumulativePower, y)
            answer = add_mod(answer, multiply_mod(container[n][jVal], cumulativePower))

        for loopJ in range(1, x + 1):
            calcAnswer(loopJ)

        return answer