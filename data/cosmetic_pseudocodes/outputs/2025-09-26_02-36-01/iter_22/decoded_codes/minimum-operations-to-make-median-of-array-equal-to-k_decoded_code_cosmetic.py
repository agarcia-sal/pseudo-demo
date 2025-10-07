class Solution:
    def minOperationsToMakeMedianK(self, nums, k):
        def ascendingSort(arr):
            i = 0
            n = len(arr)
            while i < n - 1:
                j = 0
                while j < n - i - 1:
                    if arr[j] > arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    j += 1
                i += 1

        ascendingSort(nums)

        lengthVal = len(nums)
        medIndex = 0
        while True:
            if medIndex * 2 >= lengthVal:
                break
            medIndex += 1
        medIndex -= 1

        if nums[medIndex] == k:
            return 0

        countOps = 0

        if nums[medIndex] < k:
            def incrementComparator(index, limit):
                nonlocal countOps
                if index >= limit:
                    return index
                elif nums[index] < k:
                    countOps += k - nums[index]
                    return incrementComparator(index + 1, limit)
                else:
                    return index
            incrementComparator(medIndex, lengthVal)
        else:
            def decrementComparator(index):
                nonlocal countOps
                if index < 0:
                    return index
                elif nums[index] > k:
                    countOps += nums[index] - k
                    return decrementComparator(index - 1)
                else:
                    return index
            decrementComparator(medIndex)

        return countOps