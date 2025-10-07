class Solution:
    def maximumLength(self, nums):
        frequency = {}
        for element in nums:
            frequency[element] = frequency.get(element, 0) + 1

        memo = {}

        def helper(value):
            if not (value in frequency and frequency[value] >= 2):
                if value in frequency and frequency[value] >= 1:
                    return 1
                else:
                    return 0
            if value in memo:
                return memo[value]

            squaredVal = value * value
            result = helper(squaredVal) + 2
            memo[value] = result
            return result

        maxLen = 1
        keysList = list(frequency.keys())
        idx = 0
        while idx < len(keysList):
            key = keysList[idx]
            if key == 1:
                occ = frequency[key]
                evenCount = occ - (occ % 2)
                candidate = evenCount - 1
                if candidate > maxLen:
                    maxLen = candidate
            else:
                candidate = helper(key)
                if candidate > maxLen:
                    maxLen = candidate
            idx += 1

        return maxLen