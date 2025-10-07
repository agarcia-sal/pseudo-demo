class Solution:
    def maxNumber(self, n: int) -> int:
        if n == 1:
            return 0
        tempVal = 1
        limitFlag = True

        while limitFlag:
            counterVar = tempVal
            if counterVar > n:
                limitFlag = False
            else:
                tempVal += tempVal

        counterVar = tempVal // 2
        resultVar = counterVar - 1
        return resultVar