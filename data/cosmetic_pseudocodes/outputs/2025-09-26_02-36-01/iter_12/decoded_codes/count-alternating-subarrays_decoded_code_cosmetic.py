class Solution:
    def countAlternatingSubarrays(self, nums):
        lengthVar = 0
        totalCount = 0
        sequenceStreak = 0

        def initLength():
            nonlocal lengthVar
            lengthVar = len(nums)

        def initCounters():
            nonlocal totalCount, sequenceStreak
            totalCount = lengthVar
            sequenceStreak = 1

        def addToCount(amount):
            nonlocal totalCount
            totalCount += amount

        def areDifferent(a, b):
            return a != b

        initLength()
        if lengthVar == 0:
            return 0

        initCounters()

        def loopFromIndex(currentIndex):
            nonlocal sequenceStreak
            if currentIndex >= lengthVar:
                return

            if areDifferent(nums[currentIndex], nums[currentIndex - 1]):
                sequenceStreak += 1
            else:
                sequenceStreak = 1

            addToCount(sequenceStreak - 1)
            loopFromIndex(currentIndex + 1)

        loopFromIndex(1)

        return totalCount