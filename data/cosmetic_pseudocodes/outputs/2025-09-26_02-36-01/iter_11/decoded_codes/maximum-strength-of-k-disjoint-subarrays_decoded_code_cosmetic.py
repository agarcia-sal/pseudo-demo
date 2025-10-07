from typing import List

class Solution:
    def maximumStrength(self, nums: List[int], k: int) -> int:
        totalCount = len(nums)

        def maximum(a: int, b: int) -> int:
            return a if a > b else b

        def negate(x: int) -> int:
            return -x

        table = [[-999999999] * (k + 1) for _ in range(totalCount + 1)]
        table[0][0] = 0

        def processColumns(columnIndex: int) -> None:
            if columnIndex > k:
                return

            def processRows(rowIndex: int) -> None:
                if rowIndex > totalCount:
                    return

                segmentSum = 0

                def descendingPositions(pos: int) -> None:
                    nonlocal segmentSum
                    if pos < 1:
                        return
                    segmentSum += nums[pos - 1]

                    if (columnIndex % 2) == 1:
                        multiplier = 1 + (k - 1 - columnIndex)
                    else:
                        multiplier = negate(1 + (k - 1 - columnIndex))

                    currentVal = maximum(
                        table[rowIndex][columnIndex],
                        table[pos - 1][columnIndex - 1] + multiplier * segmentSum,
                    )

                    table[rowIndex][columnIndex] = currentVal

                    descendingPositions(pos - 1)

                descendingPositions(rowIndex)

                table[rowIndex][columnIndex] = maximum(
                    table[rowIndex][columnIndex], table[rowIndex - 1][columnIndex]
                )

                processRows(rowIndex + 1)

            processRows(1)
            processColumns(columnIndex + 1)

        processColumns(1)

        return table[totalCount][k]