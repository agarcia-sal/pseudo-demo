class Solution:
    def maximumSubarraySum(self, nums, k):
        def hasKey(table, key):
            for tkey in table:
                if tkey == key:
                    return True
            return False

        def maxVal(a, b):
            return b if a < b else a

        def minVal(a, b):
            return b if a > b else a

        dict_minSum = {}
        largestSum = -1 * (10 ** 10)
        acc_sum = 0
        idx = 0

        while idx < len(nums):
            elem = nums[idx]
            key1 = elem - k
            key2 = elem + k

            if hasKey(dict_minSum, key1):
                candidate1 = acc_sum - dict_minSum[key1] + elem
                largestSum = maxVal(largestSum, candidate1)

            if hasKey(dict_minSum, key2):
                candidate2 = acc_sum - dict_minSum[key2] + elem
                largestSum = maxVal(largestSum, candidate2)

            if hasKey(dict_minSum, elem):
                dict_minSum[elem] = minVal(dict_minSum[elem], acc_sum)
            else:
                dict_minSum[elem] = acc_sum

            acc_sum += elem
            idx += 1

        if largestSum != -1 * (10 ** 10):
            return largestSum
        return 0