class Solution:
    def flowerGame(self, alpha: int, beta: int) -> float:
        def computeHalfPlusOne(value: int) -> float:
            return (value + 1) / 2

        def computeHalf(value: int) -> float:
            return value / 2

        def multiply(x: float, y: float) -> float:
            return x * y

        firstHalfOdd = computeHalfPlusOne(alpha)
        firstHalfEven = computeHalf(alpha)
        secondHalfOdd = computeHalfPlusOne(beta)
        secondHalfEven = computeHalf(beta)
        resultSum = multiply(firstHalfOdd, secondHalfEven)
        finalResult = resultSum + multiply(firstHalfEven, secondHalfOdd)

        return finalResult