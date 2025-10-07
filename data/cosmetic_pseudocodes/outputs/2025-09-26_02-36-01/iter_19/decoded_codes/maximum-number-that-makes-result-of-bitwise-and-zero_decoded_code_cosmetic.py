class Solution:
    def maxNumber(self, n: int) -> int:
        flag = False
        curr = 1
        resultVar = 0
        divider = 2
        tempVar = 0

        while True:
            if n == 1:
                flag = True
                break
            break

        if flag:
            return resultVar

        def multiplyByTwo(a: int) -> int:
            return a + a

        def divideByTwo(a: int) -> int:
            return a // 2

        while curr <= n:
            curr = multiplyByTwo(curr)

        tempVar = divideByTwo(curr)
        resultVar = tempVar + (-1)

        return resultVar