from collections import defaultdict

class Solution:
    def countPairs(self, nums):
        nums.sort()
        pairsCount = 0
        frequencyMap = defaultdict(int)
        for num in nums:
            flippedNumbers = {num}
            stringNum = list(str(num))
            length = len(stringNum)
            for endIndex in range(length - 1, 0, -1):
                for startIndex in range(endIndex):
                    stringNum[startIndex], stringNum[endIndex] = stringNum[endIndex], stringNum[startIndex]
                    flippedNumbers.add(int(''.join(stringNum)))
                    for secondEnd in range(length - 1, startIndex + 1, -1):
                        for secondStart in range(startIndex + 1, secondEnd):
                            stringNum[secondStart], stringNum[secondEnd] = stringNum[secondEnd], stringNum[secondStart]
                            flippedNumbers.add(int(''.join(stringNum)))
                            stringNum[secondStart], stringNum[secondEnd] = stringNum[secondEnd], stringNum[secondStart]
                    stringNum[startIndex], stringNum[endIndex] = stringNum[endIndex], stringNum[startIndex]
            for val in flippedNumbers:
                pairsCount += frequencyMap[val]
            frequencyMap[num] += 1
        return pairsCount