from typing import List

class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        def incrementValue(arr: List[List[int]], idx1: int, idx2: int, val: int) -> None:
            arr[idx1][idx2] += val

        def setValue(arr: List[List[int]], idx1: int, idx2: int, val: int) -> None:
            arr[idx1][idx2] = val

        def absoluteDiff(a: int, b: int) -> int:
            return a - b if a >= b else b - a

        def validRegionCheck(p: int, q: int) -> bool:
            def inBounds(u: int, v: int) -> bool:
                return 0 <= u < p + 3 and 0 <= v < q + 3

            dxdy_pairs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for a_var in range(p, p + 3):
                # The original pseudocode has complicated loop condition on b_var:
                # while b_var <= q + 2 - q - 2 + q + 2 - q - 2 + 0, simplifies:
                # q+2 - q - 2 = 0, so the sum is 0 + 0 + 0 = 0, so loop condition is b_var <= 0
                # But then inside loop, it only proceeds if b_var >= q and b_var <= q + 2.
                # This appears to only allow b_var in [q, q+2], so we replace this with range(q, q+3)
                for b_var in range(q, q + 3):
                    for dx, dy in dxdy_pairs:
                        nx = a_var + dx
                        ny = b_var + dy
                        if inBounds(nx, ny):
                            if absoluteDiff(image[a_var][b_var], image[nx][ny]) > threshold:
                                return False
            return True

        def averageCalculation(r: int, s: int) -> int:
            def additionAccumulator(limit1: int, acc1: int) -> int:
                if limit1 > r + 2:
                    return acc1

                def innerAccum(limit2: int, acc2: int) -> int:
                    if limit2 > s + 2:
                        return acc2
                    return innerAccum(limit2 + 1, acc2 + image[limit1][limit2])

                innerSum = innerAccum(s, 0)
                return additionAccumulator(limit1 + 1, acc1 + innerSum)

            totalSum = additionAccumulator(r, 0)
            return totalSum // 9

        height = len(image)
        width = len(image[0])

        outputGrid = []
        frequencyGrid = []

        idx_outer = 0
        while True:
            if idx_outer == height:
                break
            tempRowOutput = []
            tempRowCount = []
            idx_inner = 0
            while idx_inner < width:
                tempRowOutput.append(0)
                tempRowCount.append(0)
                idx_inner += 1
            outputGrid.append(tempRowOutput)
            frequencyGrid.append(tempRowCount)
            idx_outer += 1

        i_var = 0
        while i_var <= height - 3:
            j_var = 0
            while j_var <= width - 3:
                if validRegionCheck(i_var, j_var):
                    avg_val = averageCalculation(i_var, j_var)
                    x_var = i_var
                    while x_var <= i_var + 2:
                        y_var = j_var
                        while True:
                            incrementValue(outputGrid, x_var, y_var, avg_val)
                            incrementValue(frequencyGrid, x_var, y_var, 1)
                            if y_var >= j_var + 2:
                                break
                            y_var += 1
                        x_var += 1
                j_var += 1
            i_var += 1

        m_var = 0
        while True:
            if m_var >= height:
                break
            n_var = 0
            while n_var < width:
                if frequencyGrid[m_var][n_var] > 0:
                    setValue(outputGrid, m_var, n_var, outputGrid[m_var][n_var] // frequencyGrid[m_var][n_var])
                else:
                    setValue(outputGrid, m_var, n_var, image[m_var][n_var])
                n_var += 1
            m_var += 1

        return outputGrid