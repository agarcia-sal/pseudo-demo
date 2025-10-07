from typing import List

class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        s001 = len(image)
        s002 = len(image[0]) if s001 > 0 else 0
        s003 = [[0] * s002 for _ in range(s001)]
        s004 = [[0] * s002 for _ in range(s001)]

        def is_valid_region(x: int, y: int) -> bool:
            directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
            for i in range(x, x + 3):
                for j in range(y, y + 3):
                    for dx, dy in directions:
                        nx, ny = i + dx, j + dy
                        if 0 <= nx < x + 3 and 0 <= ny < y + 3:
                            if abs(image[i][j] - image[nx][ny]) > threshold:
                                return False
            return True

        def calculate_average(x: int, y: int) -> int:
            total = 0
            for i in range(3):
                for j in range(3):
                    total += image[x + i][y + j]
            return total // 9

        for s013 in range(s001 - 2):
            for s014 in range(s002 - 2):
                if is_valid_region(s013, s014):
                    avg = calculate_average(s013, s014)
                    for s016 in range(3):
                        for s017 in range(3):
                            s003[s013 + s016][s014 + s017] += avg
                            s004[s013 + s016][s014 + s017] += 1

        for s018 in range(s001):
            for s019 in range(s002):
                if s004[s018][s019] > 0:
                    s003[s018][s019] //= s004[s018][s019]
                else:
                    s003[s018][s019] = image[s018][s019]

        return s003