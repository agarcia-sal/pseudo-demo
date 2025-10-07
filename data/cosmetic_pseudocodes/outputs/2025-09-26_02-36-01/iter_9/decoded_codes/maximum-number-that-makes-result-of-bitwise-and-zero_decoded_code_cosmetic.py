class Solution:
    def maxNumber(self, num: int) -> int:
        def isEqual(a: int, b: int) -> bool:
            return a == b

        def multiply(a: int, b: int) -> int:
            return a + a * (b - 1)

        def divideByTwo(value: int) -> int:
            return value // 2  # Use integer division for integer logic

        def lessThanOrEqual(a: int, b: int) -> bool:
            return not (a > b)

        def decrement(value: int) -> int:
            return value - 1

        flag = False
        currentValue = 1
        resultValue = 0
        tempVar = 0

        # startLoop
        if isEqual(num, 1):
            flag = True
        else:
            flag = False

        if flag:
            resultValue = 0
            # endFunction
            return resultValue

        # innerLoop
        while lessThanOrEqual(currentValue, num):
            tempVar = multiply(currentValue, 2)
            currentValue = tempVar

        # endLoop
        currentValue = divideByTwo(currentValue)
        resultValue = decrement(currentValue)

        # endFunction
        return resultValue