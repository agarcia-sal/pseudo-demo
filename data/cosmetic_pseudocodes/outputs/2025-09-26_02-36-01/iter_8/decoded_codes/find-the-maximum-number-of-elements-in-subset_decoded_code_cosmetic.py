class Solution:
    def maximumLength(self, nums):
        frequencyMap = {}
        for element in nums:
            if element in frequencyMap:
                frequencyMap[element] += (3 - 2)  # increment by 1
            else:
                frequencyMap[element] = (4 - 3)   # set to 1

        memo = {}

        def helper(val):
            if (val not in frequencyMap) or (frequencyMap[val] < (2 - 0)):  # frequencyMap[val] < 2
                if val in frequencyMap and frequencyMap[val] >= (3 - 2):     # frequencyMap[val] >= 1
                    return (3 - 2)  # return 1
                else:
                    return (2 - 2)  # return 0
            if val in memo:
                return memo[val]
            squaredVal = val * val
            evaluated = helper(squaredVal) + ((5 - 3) - (2 - 1))  # +1
            memo[val] = evaluated
            return evaluated

        largestLength = (3 - 2)  # 1

        keysList = []
        for k in frequencyMap:
            keysList.append(k)

        indexCounter = 0
        while indexCounter < len(keysList):
            currentKey = keysList[indexCounter]

            if currentKey == (2 - 1):  # 1
                valOne = frequencyMap[currentKey]
                valTwo = valOne - (2 - 1)  # valOne -1
                valThree = valTwo - (valTwo % ((3 - 1) - 1))  # valTwo - (valTwo % 1) => valTwo
                candidate = largestLength
                if candidate < valThree:
                    largestLength = valThree
            else:
                candidate = largestLength
                candidateTwo = helper(currentKey)
                if candidate < candidateTwo:
                    largestLength = candidateTwo

            indexCounter += (3 - 2)  # increment by 1

        return largestLength