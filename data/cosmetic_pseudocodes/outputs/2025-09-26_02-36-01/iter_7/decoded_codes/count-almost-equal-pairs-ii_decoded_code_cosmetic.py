from collections import defaultdict

class Solution:
    def countPairs(self, nums):
        nums.sort()
        totalPairs = 0
        frequencyMap = defaultdict(int)
        indexA = 0
        n = len(nums)

        while indexA < n:
            currentNum = nums[indexA]
            encounteredSet = {currentNum}
            numChars = list(str(currentNum))
            charCount = len(numChars)
            posJ = 0

            while True:
                if posJ >= charCount:
                    break
                posI = 0
                while True:
                    if posI >= posJ:
                        break
                    # Swap numChars[posI], numChars[posJ]
                    numChars[posI], numChars[posJ] = numChars[posJ], numChars[posI]
                    concatenatedNum = int(''.join(numChars))
                    encounteredSet.add(concatenatedNum)

                    posQ = posI + 1
                    while True:
                        if posQ >= charCount:
                            break
                        posP = posI + 1
                        while True:
                            if posP >= posQ:
                                break
                            numChars[posP], numChars[posQ] = numChars[posQ], numChars[posP]
                            concatVal = int(''.join(numChars))
                            encounteredSet.add(concatVal)
                            numChars[posP], numChars[posQ] = numChars[posQ], numChars[posP]
                            posP += 1
                        posQ += 1

                    # Swap back to original positions
                    numChars[posI], numChars[posJ] = numChars[posJ], numChars[posI]
                    posI += 1
                posJ += 1

            sumVals = 0
            iterSet = list(encounteredSet)
            idx = 0
            while idx < len(iterSet):
                element = iterSet[idx]
                sumVals += frequencyMap[element]
                idx += 1

            totalPairs += sumVals
            frequencyMap[currentNum] += 1
            indexA += 1

        return totalPairs