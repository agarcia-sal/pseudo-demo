from typing import List
from math import fabs

class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        alpha = len(image)
        beta = len(image[0]) if alpha > 0 else 0

        omega = [[0 for _ in range(beta)] for _ in range(alpha)]
        sigma = [[0 for _ in range(beta)] for _ in range(alpha)]

        def is_valid_region(x: int, y: int) -> bool:
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for p in range(x, x + 3):
                for q in range(y, y + 3):
                    for deltaX, deltaY in directions:
                        candidateX = p + deltaX
                        candidateY = q + deltaY
                        if 0 <= candidateX < x + 3 and 0 <= candidateY < y + 3:
                            if abs(image[p][q] - image[candidateX][candidateY]) > threshold:
                                return False
            return True

        def calculate_average(x: int, y: int) -> int:
            aggregateSum = 0
            for r in range(x, x + 3):
                for s in range(y, y + 3):
                    aggregateSum += image[r][s]
            divisor = 9
            return aggregateSum // divisor

        for indexI in range(alpha - 2):
            for indexJ in range(beta - 2):
                if is_valid_region(indexI, indexJ):
                    avgVal = calculate_average(indexI, indexJ)
                    for posX in range(indexI, indexI + 3):
                        for posY in range(indexJ, indexJ + 3):
                            omega[posX][posY] += avgVal
                            sigma[posX][posY] += 1

        for scanI in range(alpha):
            for scanJ in range(beta):
                if sigma[scanI][scanJ] > 0:
                    omega[scanI][scanJ] = omega[scanI][scanJ] // sigma[scanI][scanJ]
                else:
                    omega[scanI][scanJ] = image[scanI][scanJ]

        return omega