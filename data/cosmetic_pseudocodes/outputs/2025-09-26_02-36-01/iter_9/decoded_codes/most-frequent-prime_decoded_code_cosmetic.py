from typing import List, Tuple, Dict

def is_prime(p: int) -> bool:
    if p <= 1:
        return False
    if p <= 3:
        return True
    if (p % 2) == 0 or (p % 3) == 0:
        return False

    def check_divisor(q: int, r: int) -> bool:
        return (q % r) == 0

    def check_divisor_plus_two(q: int, r: int) -> bool:
        return (q % (r + 2)) == 0

    iterator = 5
    while True:
        if iterator * iterator > p:
            break
        if check_divisor(p, iterator) or check_divisor_plus_two(p, iterator):
            return False
        iterator += 6
    return True

class Solution:
    def mostFrequentPrime(self, matrix: List[List[int]]) -> int:
        rowCount = len(matrix)
        colCount = len(matrix[0]) if rowCount > 0 else 0

        directionsList: List[Tuple[int, int]] = [(-1, 0), (-1, 1), (0, 1), (1, 1),
                                                (1, 0), (1, -1), (0, -1), (-1, -1)]

        primeMap: Dict[int, int] = {}

        def dfs(posX: int, posY: int, deltaX: int, deltaY: int, collectedNumber: int) -> None:
            nextX = posX + deltaX
            nextY = posY + deltaY

            if 0 <= nextX < rowCount and 0 <= nextY < colCount:
                appendedNumber = collectedNumber * 10 + matrix[nextX][nextY]
                if appendedNumber > 10 and is_prime(appendedNumber):
                    primeMap[appendedNumber] = primeMap.get(appendedNumber, 0) + 1
                dfs(nextX, nextY, deltaX, deltaY, appendedNumber)

        def iterateOverMatrix() -> None:
            for r in range(rowCount):
                for c in range(colCount):
                    for deltaX, deltaY in directionsList:
                        dfs(r, c, deltaX, deltaY, matrix[r][c])

        iterateOverMatrix()

        if not primeMap:
            return -1

        maxCount = -1
        resultPrime = -1
        for key, val in primeMap.items():
            if val > maxCount:
                maxCount = val
                resultPrime = key

        return resultPrime