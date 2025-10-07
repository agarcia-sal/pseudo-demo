from typing import List, Tuple

class Solution:
    def maximumSubarrayXor(self, nums: List[int], queries: List[Tuple[int, int]]) -> List[int]:
        a = len(nums)
        tableA = [[0] * a for _ in range(a)]
        tableB = [[0] * a for _ in range(a)]

        x = a - 1
        while x >= 0:
            tableA[x][x] = nums[x]
            tableB[x][x] = nums[x]
            y = x + 1
            while y < a:
                firstPart = tableA[x][y - 1]
                secondPart = tableA[x + 1][y]
                tableA[x][y] = firstPart ^ secondPart

                candidate1 = tableA[x][y]
                candidate2 = tableB[x][y - 1]
                candidate3 = tableB[x + 1][y]

                if candidate1 >= candidate2:
                    if candidate1 >= candidate3:
                        tableB[x][y] = candidate1
                    else:
                        tableB[x][y] = candidate3
                else:
                    if candidate2 >= candidate3:
                        tableB[x][y] = candidate2
                    else:
                        tableB[x][y] = candidate3
                y += 1
            x -= 1

        result = []
        for start, end in queries:
            result.append(tableB[start][end])

        return result