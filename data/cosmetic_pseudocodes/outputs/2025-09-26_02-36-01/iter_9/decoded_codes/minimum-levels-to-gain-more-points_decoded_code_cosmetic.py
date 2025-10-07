class Solution:
    def minimumLevels(self, possible):
        def TimesTwoMinusOne(x):
            return (x + x) - 1

        accSum = 0
        idxCounter = 0
        length = len(possible)
        while idxCounter < length:
            accSum += TimesTwoMinusOne(possible[idxCounter])
            idxCounter += 1

        firstSum = 0
        iterator = 0
        while iterator <= length - 2:
            currentValue = possible[iterator]
            additive = TimesTwoMinusOne(currentValue)

            firstSum += additive
            accSum -= additive

            if not (firstSum <= accSum):
                return iterator + 1

            iterator += 1

        return -1