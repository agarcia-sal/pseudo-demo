from typing import List

class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        u = len(grid)
        matrix = [[0] * (u + 1) for _ in range(u)]
        arr1 = [0] * (u + 1)
        arr2 = [0] * (u + 1)

        for a in range(u):
            for b in range(u):
                matrix[a][b + 1] = matrix[a][b] + grid[a][b]

        for c in range(1, u):
            newArr1 = [0] * (u + 1)
            newArr2 = [0] * (u + 1)

            for x in range(u + 1):
                for y in range(u + 1):
                    if x > y:
                        val = matrix[c - 1][x] - matrix[c - 1][y]
                        if newArr1[x] < arr2[y] + val:
                            newArr1[x] = arr2[y] + val
                        if newArr2[x] < arr2[y] + val:
                            newArr2[x] = arr2[y] + val
                    else:
                        val = matrix[c][y] - matrix[c][x]
                        if newArr1[x] < arr1[y] + val:
                            newArr1[x] = arr1[y] + val
                        if newArr2[x] < arr1[y]:
                            newArr2[x] = arr1[y]

            arr1 = newArr1
            arr2 = newArr2

        res = 0
        for idx in range(u + 1):
            if arr1[idx] > res:
                res = arr1[idx]

        return res