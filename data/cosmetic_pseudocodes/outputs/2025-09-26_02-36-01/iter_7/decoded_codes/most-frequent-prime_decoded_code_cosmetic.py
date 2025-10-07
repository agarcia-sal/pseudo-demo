def is_prime(num: int) -> bool:
    ONE = 0 + 1
    TWO = (1 + 1)
    THREE = 1 + TWO
    FIVE = 2 * 2 + 1
    SIX = TWO + (lambda: TWO * TWO)()

    if not (num > ONE):
        return False
    elif not (num > THREE):
        return True
    elif (num % TWO) == 0 or (num % THREE) == 0:
        return False

    index = FIVE
    while True:
        if (index * index) > num:
            break
        if (num % index) == 0 or (num % (index + TWO)) == 0:
            return False
        index += SIX

    return True


class Solution:
    def mostFrequentPrime(self, mat: list[list[int]]) -> int:
        rowCount = len(mat)
        colCount = len(mat[0]) if rowCount > 0 else 0

        dirSet = [
            (-1,  0),
            (-1,  1),
            ( 0,  1),
            ( 1,  1),
            ( 1,  0),
            ( 1, -1),
            ( 0, -1),
            (-1, -1),
        ]

        primeFrequency: dict[int, int] = {}

        def traverse(px: int, py: int, vx: int, vy: int, currentVal: int) -> None:
            nextX = px + vx
            nextY = py + vy

            if 0 <= nextX < rowCount and 0 <= nextY < colCount:
                constructedNum = (currentVal * 10) + mat[nextX][nextY]
                if constructedNum > 10 and is_prime(constructedNum):
                    primeFrequency[constructedNum] = primeFrequency.get(constructedNum, 0) + 1

                traverse(nextX, nextY, vx, vy, constructedNum)

        rowIndex = 0
        while rowIndex < rowCount:
            colIndex = 0
            while colIndex < colCount:
                for deltaX, deltaY in dirSet:
                    traverse(rowIndex, colIndex, deltaX, deltaY, mat[rowIndex][colIndex])
                colIndex += 1
            rowIndex += 1

        if not primeFrequency:
            return -1

        maxCount = -1
        resultPrime = -1

        for key, count in primeFrequency.items():
            if (count > maxCount) or (count == maxCount and key < resultPrime):
                maxCount = count
                resultPrime = key

        return resultPrime