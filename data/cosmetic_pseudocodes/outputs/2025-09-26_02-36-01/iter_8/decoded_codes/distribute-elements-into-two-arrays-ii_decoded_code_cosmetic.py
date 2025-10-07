class Solution:
    def resultArray(self, nums):
        # Initialize betaList and deltaList starting with nums[0] and nums[1] respectively
        betaList = [nums[0]]
        deltaList = [nums[1]]
        gammaSorted = [nums[0]]
        epsilonSorted = [nums[1]]

        def greaterCount(sequence, pivot):
            # Binary search to find how many elements in sequence are greater than pivot
            start, end = 0, len(sequence)
            while start < end:
                mid = (start + end) // 2
                if pivot < sequence[mid]:
                    end = mid
                else:
                    start = mid + 1
            return len(sequence) - start

        indexOmega = 2
        while indexOmega <= len(nums) - 1:
            zetaVal = nums[indexOmega]

            sigmaCount = greaterCount(gammaSorted, zetaVal)
            tauCount = greaterCount(epsilonSorted, zetaVal)

            if sigmaCount > tauCount:
                betaList.append(zetaVal)

                # Insert maintaining sorted order in gammaSorted
                i = 0
                while i < len(gammaSorted) and gammaSorted[i] < zetaVal:
                    i += 1
                gammaSorted.insert(i, zetaVal)

            elif sigmaCount < tauCount:
                deltaList.append(zetaVal)

                # Insert maintaining sorted order in epsilonSorted
                j = 0
                while j < len(epsilonSorted) and epsilonSorted[j] < zetaVal:
                    j += 1
                epsilonSorted.insert(j, zetaVal)

            else:
                if len(betaList) <= len(deltaList):
                    betaList.append(zetaVal)

                    # Insert maintaining sorted order in gammaSorted
                    k = 0
                    while k < len(gammaSorted) and gammaSorted[k] < zetaVal:
                        k += 1
                    gammaSorted.insert(k, zetaVal)
                else:
                    deltaList.append(zetaVal)

                    # Insert maintaining sorted order in epsilonSorted
                    m = 0
                    while m < len(epsilonSorted) and epsilonSorted[m] < zetaVal:
                        m += 1
                    epsilonSorted.insert(m, zetaVal)

            indexOmega += 1

        finalResult = []
        for val in betaList:
            finalResult.append(val)
        for val in deltaList:
            finalResult.append(val)

        return finalResult