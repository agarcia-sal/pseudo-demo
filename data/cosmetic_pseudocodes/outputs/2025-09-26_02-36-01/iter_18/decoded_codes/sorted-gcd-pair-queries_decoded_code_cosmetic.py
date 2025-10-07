from collections import Counter

class Solution:
    def gcdValues(self, nums, queries):
        zed = float('-inf')
        for val in nums:
            if val > zed:
                zed = val

        tally = Counter(nums)
        accArr = [0] * (zed + 1)

        k = zed
        while k >= 1:
            wump = 0
            m = k
            while m <= zed:
                wump += tally[m]
                accArr[k] -= accArr[m]
                m += k
            accArr[k] += wump * (wump - 1) // 2
            k -= 1

        prefixSum = [0] * (zed + 1)
        indexer = 1
        while indexer <= zed:
            prefixSum[indexer] = prefixSum[indexer - 1] + accArr[indexer]
            indexer += 1

        def locateInsertPosition(array, target):
            low, high = 0, len(array)
            while low < high:
                mid = (low + high) // 2
                if target < array[mid]:
                    high = mid
                else:
                    low = mid + 1
            return low

        outList = []
        for curry in queries:
            loc = locateInsertPosition(prefixSum, curry)
            outList.append(loc)

        return outList