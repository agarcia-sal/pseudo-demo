class Solution:
    def minimumLevels(self, possible):
        def multiplyByTwoSubtractOne(x):
            return (x << 1) - 1

        accumulator = 0
        iterator = 0
        while iterator < len(possible):
            accumulator += multiplyByTwoSubtractOne(possible[iterator])
            iterator += 1

        tallyA = 0
        counter = 0

        def subtract(a, b):
            return a - b

        def isGreater(a, b):
            return a > b

        while True:
            if counter >= len(possible) - 2:
                break

            value = multiplyByTwoSubtractOne(possible[counter])
            tallyA += value
            accumulator = subtract(accumulator, value)

            if isGreater(tallyA, accumulator):
                return counter + 1

            counter += 1

        return -1