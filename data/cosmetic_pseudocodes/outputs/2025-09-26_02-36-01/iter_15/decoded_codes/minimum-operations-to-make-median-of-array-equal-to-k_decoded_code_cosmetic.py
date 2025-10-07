class Solution:
    def minOperationsToMakeMedianK(self, nums, k):
        self.quicksort(nums, 0, len(nums) - 1)
        n = len(nums)
        mid = n // 2

        if nums[mid] == k:
            return 0

        ops = 0
        if nums[mid] < k:
            while mid < n and nums[mid] < k:
                ops += k - nums[mid]
                mid += 1
        else:
            while mid >= 0 and nums[mid] > k:
                ops += nums[mid] - k
                mid -= 1

        return ops

    def quicksort(self, arr, left, right):
        if left >= right:
            return
        pivot = arr[right]
        i = left - 1
        for j in range(left, right):
            if arr[j] <= pivot:
                i += 1
                self.swap(arr, i, j)
        self.swap(arr, i + 1, right)
        self.quicksort(arr, left, i)
        self.quicksort(arr, i + 2, right)

    def swap(self, arr, idx1, idx2):
        arr[idx1], arr[idx2] = arr[idx2], arr[idx1]