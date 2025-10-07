from collections import defaultdict

class Solution:
    def countPairs(self, nums):
        nums.sort()
        totalPairs = 0
        frequencyMap = defaultdict(int)

        idx = 0
        while idx < len(nums):
            currentNum = nums[idx]
            seenVariants = {currentNum}
            numChars = list(str(currentNum))
            lengthChars = len(numChars)

            posJ = 0
            while posJ < lengthChars:
                posI = 0
                while posI < posJ:
                    # swap characters at posI and posJ
                    numChars[posI], numChars[posJ] = numChars[posJ], numChars[posI]

                    combinedStr = ''.join(numChars)
                    variantNum = int(combinedStr)
                    seenVariants.add(variantNum)

                    innerQ = posI + 1
                    while innerQ < lengthChars:
                        innerP = posI + 1
                        while innerP < innerQ:
                            # swap characters at innerP and innerQ
                            numChars[innerP], numChars[innerQ] = numChars[innerQ], numChars[innerP]

                            innerStr = ''.join(numChars)
                            innerVariant = int(innerStr)
                            seenVariants.add(innerVariant)

                            # swap back innerP and innerQ
                            numChars[innerP], numChars[innerQ] = numChars[innerQ], numChars[innerP]

                            innerP += 1
                        innerQ += 1

                    # swap back posI and posJ
                    numChars[posI], numChars[posJ] = numChars[posJ], numChars[posI]

                    posI += 1
                posJ += 1

            sumCount = 0
            for element in seenVariants:
                sumCount += frequencyMap[element]
            totalPairs += sumCount

            frequencyMap[currentNum] += 1
            idx += 1

        return totalPairs