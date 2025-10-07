class Solution:
    def minimumLevels(self, possible):
        def multiplyByTwo(value):
            return value << 1

        acc = 0
        iterator = 0

        while iterator < len(possible):
            val = possible[iterator]
            tmp = multiplyByTwo(val) - 1
            acc += tmp
            iterator += 1

        sumA = 0
        i = 0
        while i < len(possible):
            currentVal = possible[i]
            dVal = multiplyByTwo(currentVal) - 1

            sumA += dVal
            acc -= dVal

            if sumA > acc:
                return i + 1

            i += 1

        return -1