class Solution:
    def maximumLength(self, nums):
        evenCount = 0
        oddCount = 0
        index = 1
        while index < len(nums):
            sumAdjacent = nums[index - 1] + nums[index]
            if sumAdjacent % 2 == 0:
                tempEven = evenCount + 1
                if tempEven > oddCount:
                    evenCount = tempEven
                else:
                    evenCount = oddCount
            else:
                tempOdd = oddCount + 1
                if tempOdd > evenCount:
                    oddCount = tempOdd
                else:
                    oddCount = evenCount
            index += 1

        maxLengthCandidate1 = evenCount
        maxLengthCandidate2 = oddCount + 1
        if maxLengthCandidate1 > maxLengthCandidate2:
            return maxLengthCandidate1
        else:
            return maxLengthCandidate2