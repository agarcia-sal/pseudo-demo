def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    def loop_check(d: int) -> bool:
        if d * d > n:
            return True
        if n % d == 0 or n % (d + 2) == 0:
            return False
        return loop_check(d + 6)

    return loop_check(5)


class Solution:
    def mostFrequentPrime(self, mat: list[list[int]]) -> int:
        rowCount = len(mat)
        colCount = len(mat[0]) if mat else 0
        dirOffsets = [(-1, 0), (-1, 1), (0, 1), (1, 1),
                      (1, 0), (1, -1), (0, -1), (-1, -1)]
        primeFreq = {}

        def traverse(posX: int, posY: int, deltaX: int, deltaY: int, currNum: int):
            nextX = posX + deltaX
            nextY = posY + deltaY
            if 0 <= nextX < rowCount and 0 <= nextY < colCount:
                updatedNum = currNum * 10 + mat[nextX][nextY]
                if updatedNum > 10 and is_prime(updatedNum):
                    primeFreq[updatedNum] = primeFreq.get(updatedNum, 0) + 1
                traverse(nextX, nextY, deltaX, deltaY, updatedNum)

        for rowIndex in range(rowCount):
            for colIndex in range(colCount):
                for deltaX, deltaY in dirOffsets:
                    traverse(rowIndex, colIndex, deltaX, deltaY, mat[rowIndex][colIndex])

        maxPrime = -1
        if primeFreq:
            keys = list(primeFreq.keys())

            def compare_keys(keyList: list[int]) -> int | None:
                if not keyList:
                    return None
                if len(keyList) == 1:
                    return keyList[0]
                head = keyList[0]
                tailMax = compare_keys(keyList[1:])
                headCount = primeFreq[head]
                tailCount = primeFreq[tailMax]
                if headCount > tailCount or (headCount == tailCount and head > tailMax):
                    return head
                else:
                    return tailMax

            cmpResult = compare_keys(keys)
            if cmpResult is not None:
                maxPrime = cmpResult

        return maxPrime