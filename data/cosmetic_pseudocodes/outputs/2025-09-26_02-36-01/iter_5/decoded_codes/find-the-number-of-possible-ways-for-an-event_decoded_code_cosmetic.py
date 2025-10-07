class Solution:
    def numberOfWays(self, n: int, x: int, y: int) -> int:
        constant_mod = 10**9 + 7

        def buildMatrix(rowCount: int, colCount: int):
            if rowCount == 0:
                return []
            else:
                return [[0] * colCount] + buildMatrix(rowCount - 1, colCount)

        table = buildMatrix(n + 1, x + 1)
        table[0][0] = 1

        def outerLoop(current_row: int):
            if current_row > n:
                return
            def innerLoop(current_col: int):
                if current_col > x:
                    return
                prevRowSameCol = table[current_row - 1][current_col]
                prevRowPrevCol = table[current_row - 1][current_col - 1] if current_col - 1 >= 0 else 0
                left_factor = (prevRowSameCol * current_col) % constant_mod
                right_factor = (prevRowPrevCol * (x - (current_col - 1))) % constant_mod
                table[current_row][current_col] = (left_factor + right_factor) % constant_mod
                innerLoop(current_col + 1)
            innerLoop(1)
            outerLoop(current_row + 1)

        outerLoop(1)

        result_accumulator = 0
        power_accumulator = 1

        def accumulate(j_counter: int):
            nonlocal result_accumulator, power_accumulator
            if j_counter > x:
                return
            power_accumulator = (power_accumulator * y) % constant_mod
            term = (table[n][j_counter] * power_accumulator) % constant_mod
            result_accumulator = (result_accumulator + term) % constant_mod
            accumulate(j_counter + 1)

        accumulate(1)

        final_result = result_accumulator
        return final_result