from typing import List

class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0]) if rows > 0 else 0

        sums = [[0] * cols for _ in range(rows)]
        occurrences = [[0] * cols for _ in range(rows)]

        def is_valid_region(x: int, y: int) -> bool:
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            # Check all pixels in the 3x3 block starting at (x, y)
            for row in range(x, x + 3):
                for col in range(y, y + 3):
                    for dx, dy in directions:
                        nx, ny = row + dx, col + dy
                        # Neighbor pixel must be inside the 3x3 block
                        if x <= nx < x + 3 and y <= ny < y + 3:
                            if abs(image[row][col] - image[nx][ny]) > threshold:
                                return False
            return True

        def calculate_average(x: int, y: int) -> int:
            total_sum = 0
            for row in range(x, x + 3):
                for col in range(y, y + 3):
                    total_sum += image[row][col]
            return total_sum // 9

        for i in range(rows - 2):
            for j in range(cols - 2):
                if is_valid_region(i, j):
                    avg_val = calculate_average(i, j)
                    for r in range(i, i + 3):
                        for c in range(j, j + 3):
                            sums[r][c] += avg_val
                            occurrences[r][c] += 1

        for i in range(rows):
            for j in range(cols):
                if occurrences[i][j] > 0:
                    sums[i][j] //= occurrences[i][j]
                else:
                    sums[i][j] = image[i][j]

        return sums