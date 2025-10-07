from typing import List

class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0]) if m > 0 else 0
        result = [[0] * n for _ in range(m)]
        count = [[0] * n for _ in range(m)]

        def is_valid_region(x: int, y: int) -> bool:
            neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for i in range(x, x + 3):
                for j in range(y, y + 3):
                    for dx, dy in neighbors:
                        nx = i + dx
                        ny = j + dy
                        if 0 <= nx < x + 3 and 0 <= ny < y + 3:
                            if abs(image[i][j] - image[nx][ny]) > threshold:
                                return False
            return True

        def calculate_average(x: int, y: int) -> int:
            total = 0
            for i in range(x, x + 3):
                for j in range(y, y + 3):
                    total += image[i][j]
            return total // 9

        # Iterate over all possible 3x3 subregions inside the image bounds
        for i in range(m - 2):
            for j in range(n - 2):
                if is_valid_region(i, j):
                    avg = calculate_average(i, j)
                    for x in range(i, i + 3):
                        for y in range(j, j + 3):
                            result[x][y] += avg
                            count[x][y] += 1

        for i in range(m):
            for j in range(n):
                if count[i][j] > 0:
                    result[i][j] //= count[i][j]
                else:
                    result[i][j] = image[i][j]

        return result