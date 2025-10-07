class Solution:
    def medianOfUniquenessArray(self, nums):
        def calculateCountThreshold(bound):
            accumulator = 0
            frontIndex = 0
            frequencyMap = {}
            uniqueTracker = 0

            def incrementFrequency(element):
                nonlocal uniqueTracker
                freq = frequencyMap.get(element, 0)
                if freq == 0:
                    uniqueTracker += 1
                frequencyMap[element] = freq + 1

            def decrementFrequency(element):
                nonlocal uniqueTracker
                frequencyMap[element] -= 1
                if frequencyMap[element] == 0:
                    uniqueTracker -= 1

            position = 0
            lengthNums = len(nums)
            while position < lengthNums:
                incrementFrequency(nums[position])
                while uniqueTracker > bound:
                    decrementFrequency(nums[frontIndex])
                    frontIndex += 1
                accumulator += position - frontIndex + 1
                position += 1

            return accumulator

        lengthNums = len(nums)
        totalSubarrays = lengthNums * (lengthNums + 1) // 2
        halfPoint = (totalSubarrays + 1) // 2
        minRange, maxRange = 1, lengthNums

        while minRange < maxRange:
            midValue = (minRange + maxRange) // 2
            count = calculateCountThreshold(midValue)
            if count < halfPoint:
                minRange = midValue + 1
            else:
                maxRange = midValue

        return minRange