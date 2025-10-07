from math import gcd

class Solution:
    def subsequencePairCount(self, nums):
        LIMIT = 1_000_000_007
        topVal = float('-inf')
        for num in nums:
            if num > topVal:
                topVal = num

        def createMatrix(rows, cols):
            return [[0] * cols for _ in range(rows)]

        table = createMatrix(topVal + 1, topVal + 1)
        table[0][0] = 1

        for currentNum in nums:
            updatedTbl = createMatrix(topVal + 1, topVal + 1)
            for outer in range(topVal + 1):
                for inner in range(topVal + 1):
                    tempVal = table[outer][inner]
                    if tempVal == 0:
                        continue
                    updatedTbl[outer][inner] = (updatedTbl[outer][inner] + tempVal) % LIMIT

                    newO = gcd(outer, currentNum)
                    updatedTbl[newO][inner] = (updatedTbl[newO][inner] + tempVal) % LIMIT

                    newI = gcd(inner, currentNum)
                    updatedTbl[outer][newI] = (updatedTbl[outer][newI] + tempVal) % LIMIT
            table = updatedTbl

        accumulator = 0
        for count in range(1, topVal + 1):
            accumulator += table[count][count]

        return accumulator % LIMIT