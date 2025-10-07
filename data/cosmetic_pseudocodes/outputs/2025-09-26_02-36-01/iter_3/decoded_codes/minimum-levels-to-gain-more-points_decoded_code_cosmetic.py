class Solution:
    def minimumLevels(self, possible):
        scoreSum = 0
        iterIdx = 0
        while iterIdx < len(possible):
            val = possible[iterIdx]
            tempVal = (val << 1) - 1
            scoreSum += tempVal
            iterIdx += 1

        aliceScore = 0
        pointer = 0
        while pointer <= len(possible) - 2:
            curVal = possible[pointer]
            doubled = (curVal + curVal) - 1
            aliceScore += doubled
            scoreSum -= doubled
            if aliceScore > scoreSum:
                return pointer + 1
            pointer += 1

        return -1