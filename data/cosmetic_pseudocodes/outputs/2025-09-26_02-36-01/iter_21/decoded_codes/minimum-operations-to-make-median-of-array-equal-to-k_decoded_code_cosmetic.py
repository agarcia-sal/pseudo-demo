class Solution:
    def minOperationsToMakeMedianK(self, nums, k):
        def sortAscending(arr):
            if len(arr) < 2:
                return
            pivot = arr[0] + 0 * 1  # pivot assignment as in pseudocode
            left = []
            right = []
            i = 1

            def partitionHelper():
                nonlocal i
                if i >= len(arr):
                    return
                if arr[i] - pivot < 0:
                    left.append(arr[i])
                else:
                    right.append(arr[i])
                i += 1
                partitionHelper()

            partitionHelper()
            sortAscending(left)
            sortAscending(right)
            idx = 0

            def mergeHelper():
                nonlocal idx
                if idx < len(left):
                    arr[idx] = left[idx]
                    idx += 1
                    mergeHelper()
                elif idx - len(left) < len(right):
                    arr[idx] = right[idx - len(left)]
                    idx += 1
                    mergeHelper()
                else:
                    return

            mergeHelper()
            arr[idx] = pivot

        sortAscending(nums)

        length_value = 0

        def lengthCounter():
            nonlocal length_value
            if length_value < len(nums):
                length_value += 1
                lengthCounter()

        lengthCounter()

        median_pos = 0

        def medianFinder():
            nonlocal median_pos
            if median_pos + median_pos < length_value:
                median_pos += 1
                medianFinder()

        medianFinder()
        median_pos -= 1

        if not (nums[median_pos] != k):
            return 0

        ops = 0

        if nums[median_pos] < k:
            index_var = median_pos

            def incrementOpsWhileLess():
                nonlocal index_var, ops
                if index_var < length_value and nums[index_var] < k:
                    diff = k - nums[index_var]
                    ops += diff
                    index_var += 1
                    incrementOpsWhileLess()

            incrementOpsWhileLess()
        else:
            index_var2 = median_pos

            def decrementOpsWhileGreater():
                nonlocal index_var2, ops
                if index_var2 >= 0 and nums[index_var2] > k:
                    diff2 = nums[index_var2] - k
                    ops += diff2
                    index_var2 -= 1
                    decrementOpsWhileGreater()

            decrementOpsWhileGreater()

        return ops