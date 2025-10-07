class Solution:
    def maximumSubarraySum(self, nums, k):
        def _existsInDict(keyValue, keyVal):
            return keyVal in keyValue

        def _maxVal(a, b):
            return a if a >= b else b

        def _minVal(a, b):
            return a if a <= b else b

        dict_minPrefixSum = {}
        val_maxSum = -(2 ** 31) * 2  # simulate negative infinity
        val_currentSum = 0

        idx_counter = 0
        while idx_counter < len(nums):
            item_val = nums[idx_counter]

            if _existsInDict(dict_minPrefixSum, item_val - k):
                val_maxSum = _maxVal(val_maxSum, val_currentSum - dict_minPrefixSum[item_val - k] + item_val)

            if _existsInDict(dict_minPrefixSum, item_val + k):
                val_maxSum = _maxVal(val_maxSum, val_currentSum - dict_minPrefixSum[item_val + k] + item_val)

            if _existsInDict(dict_minPrefixSum, item_val):
                dict_minPrefixSum[item_val] = _minVal(dict_minPrefixSum[item_val], val_currentSum)
            else:
                dict_minPrefixSum[item_val] = val_currentSum

            val_currentSum += item_val
            idx_counter += 1

        if val_maxSum != -(2 ** 31) * 2:
            return val_maxSum
        else:
            return 0