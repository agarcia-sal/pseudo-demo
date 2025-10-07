class Solution:
    def minimumLevels(self, possible):
        sumScores = 0
        iterator = 0
        length = len(possible)
        while iterator < length:
            currentVal = possible[iterator]
            incrementValue = (currentVal * 2) - 1
            sumScores += incrementValue
            iterator += 1

        aliceSum = 0
        position = 0
        while position < length - 1:
            val = possible[position]
            incValue = (val * 2) - 1
            aliceSum += incValue
            sumScores -= incValue

            if aliceSum > sumScores:
                return position + 1
            position += 1

        return -1