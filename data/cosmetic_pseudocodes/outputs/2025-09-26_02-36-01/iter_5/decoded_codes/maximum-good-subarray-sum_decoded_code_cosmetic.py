class Solution:
    def maximumSubarraySum(self, nums, k):
        def helper(index, total, minPref, maxVal):
            if index == len(nums):
                return maxVal
            currentElement = nums[index]
            candidateVals = []
            if currentElement - k in minPref:
                val1 = total - minPref[currentElement - k] + currentElement
                candidateVals.append(val1)
            if currentElement + k in minPref:
                val2 = total - minPref[currentElement + k] + currentElement
                candidateVals.append(val2)
            newMax = maxVal
            for v in candidateVals:
                if v > newMax:
                    newMax = v
            if currentElement in minPref:
                existingMin = minPref[currentElement]
                if total < existingMin:
                    minPref[currentElement] = total
            else:
                minPref[currentElement] = total
            return helper(index + 1, total + currentElement, minPref, newMax)

        NEG_INF = float('-inf')
        resultMax = helper(0, 0, {}, NEG_INF)
        return resultMax if resultMax != NEG_INF else 0