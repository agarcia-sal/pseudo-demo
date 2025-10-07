from typing import List, Dict, Tuple, Optional


def is_prime(number: int) -> bool:
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    idx = 5
    while idx * idx <= number:
        if number % idx == 0 or number % (idx + 2) == 0:
            return False
        idx += 6
    return True


class Solution:
    def mostFrequentPrime(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        directionsList: List[Tuple[int, int]] = [
            (-1, 0), (-1, 1), (0, 1), (1, 1),
            (1, 0), (1, -1), (0, -1), (-1, -1)
        ]
        countsMap: Dict[int, int] = {}

        def traverse(posX: int, posY: int, stepX: int, stepY: int, numSoFar: int):
            nextX = posX + stepX
            nextY = posY + stepY
            if 0 <= nextX < rows and 0 <= nextY < cols:
                updatedNum = numSoFar * 10 + matrix[nextX][nextY]
                if updatedNum > 10 and is_prime(updatedNum):
                    countsMap[updatedNum] = countsMap.get(updatedNum, 0) + 1
                traverse(nextX, nextY, stepX, stepY, updatedNum)

        for rowIndex in range(rows):
            for colIndex in range(cols):
                for dx, dy in directionsList:
                    traverse(rowIndex, colIndex, dx, dy, matrix[rowIndex][colIndex])

        if not countsMap:
            return -1

        maxPrime: Optional[int] = None
        maxCount = -1
        for primeKey, currentCount in countsMap.items():
            if (currentCount > maxCount) or (currentCount == maxCount and (maxPrime is None or primeKey > maxPrime)):
                maxCount = currentCount
                maxPrime = primeKey

        return maxPrime