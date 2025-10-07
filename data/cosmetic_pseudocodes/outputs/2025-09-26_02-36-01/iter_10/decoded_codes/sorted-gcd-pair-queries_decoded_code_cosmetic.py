class Solution:
    def gcdValues(self, nums, queries):
        def findMaximum(numbers):
            totalMax = numbers[0]
            idx = 1
            while idx < len(numbers):
                if numbers[idx] > totalMax:
                    totalMax = numbers[idx]
                idx += 1
            return totalMax

        def initializeCounter(numbers):
            tally = {}
            pos = 0
            while pos < len(numbers):
                if numbers[pos] in tally:
                    tally[numbers[pos]] += 1
                else:
                    tally[numbers[pos]] = 1
                pos += 1
            return tally

        def makeZeroList(lengthVal):
            zeroList = []
            counterIndex = 0
            while counterIndex != lengthVal:
                zeroList.append(0)
                counterIndex += 1
            return zeroList

        def bisectRight(accumArr, val):
            low = 0
            high = len(accumArr)
            while low < high:
                mid = (low + high) // 2
                if accumArr[mid] > val:
                    high = mid
                else:
                    low = mid + 1
            return low

        maximumValue = findMaximum(nums)
        counterMap = initializeCounter(nums)
        counting_gcd = makeZeroList(maximumValue + 1)

        def processIndex(currIndex):
            tempVal = 0

            def innerLoop(subIndex):
                nonlocal tempVal
                if subIndex > maximumValue:
                    return
                if subIndex % currIndex == 0:
                    if subIndex in counterMap:
                        tempVal += counterMap[subIndex]
                    counting_gcd[currIndex] -= counting_gcd[subIndex]
                innerLoop(subIndex + currIndex)

            innerLoop(currIndex)
            counting_gcd[currIndex] += (tempVal * (tempVal - 1)) // 2

        def loopDownwards(num):
            if num < 1:
                return
            processIndex(num)
            loopDownwards(num - 1)

        loopDownwards(maximumValue)

        def accumulateList(sourceList):
            accList = makeZeroList(len(sourceList))
            ind = 1
            while ind < len(sourceList):
                accList[ind] = accList[ind - 1] + sourceList[ind]
                ind += 1
            return accList

        accumulator = accumulateList(counting_gcd)
        outputList = []

        def processQueries(index):
            if index >= len(queries):
                return
            outputList.append(bisectRight(accumulator, queries[index]))
            processQueries(index + 1)

        processQueries(0)
        return outputList