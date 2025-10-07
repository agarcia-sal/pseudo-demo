from collections import defaultdict

class Solution:
    def countPairs(self, nums):
        def replicateSort(S):
            indexA = 0
            while indexA < len(S) - 1:
                indexB = indexA + 1
                while indexB < len(S):
                    if not (S[indexA] <= S[indexB]):
                        S[indexA], S[indexB] = S[indexB], S[indexA]
                    indexB += 1
                indexA += 1

        replicateSort(nums)

        resultCount = 0
        frequencyMap = defaultdict(int)

        indexOuter = 0
        while indexOuter < len(nums):
            elementSet = set()
            baseNumber = nums[indexOuter]
            elementSet.add(baseNumber)

            digitList = [d for d in str(baseNumber)]
            lenDigits = len(digitList)

            posJ = 0
            while posJ < lenDigits:
                posI = 0
                while posI < posJ:
                    # Swap digits at posI and posJ
                    digitList[posI], digitList[posJ] = digitList[posJ], digitList[posI]

                    concatenatedString = ''.join(digitList)
                    elementSet.add(int(concatenatedString))

                    qIndex = posI + 1
                    while qIndex < lenDigits:
                        pIndex = posI + 1
                        while pIndex < qIndex:
                            # Swap digits at pIndex and qIndex
                            digitList[pIndex], digitList[qIndex] = digitList[qIndex], digitList[pIndex]

                            concatStrInner = ''.join(digitList)
                            elementSet.add(int(concatStrInner))

                            # Revert inner swap
                            digitList[pIndex], digitList[qIndex] = digitList[qIndex], digitList[pIndex]
                            pIndex += 1
                        qIndex += 1

                    # Revert the outer swap
                    digitList[posI], digitList[posJ] = digitList[posJ], digitList[posI]
                    posI += 1
                posJ += 1

            sumIncrement = 0
            for item in elementSet:
                sumIncrement += frequencyMap[item]

            resultCount += sumIncrement
            frequencyMap[baseNumber] += 1
            indexOuter += 1

        return resultCount