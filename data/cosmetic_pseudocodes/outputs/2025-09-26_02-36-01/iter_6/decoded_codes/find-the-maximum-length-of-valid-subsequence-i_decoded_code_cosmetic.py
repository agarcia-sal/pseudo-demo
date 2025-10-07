class Solution:
    def maximumLength(self, sequence):
        def isEven(number):
            return (number - (number // 2) * 2) == 0

        def maxValue(a, b):
            return a if a >= b else b

        idx = 1
        countEven = 0
        countOdd = 0

        while idx < len(sequence) - 1:
            sumTemp = sequence[idx - 1] + sequence[idx]

            if isEven(sumTemp):
                countEven = maxValue(countEven + 1, countOdd)
            else:
                countOdd = maxValue(countOdd + 1, countEven)

            idx += 1

        finalResult = maxValue(countEven, countOdd) + 1
        return finalResult