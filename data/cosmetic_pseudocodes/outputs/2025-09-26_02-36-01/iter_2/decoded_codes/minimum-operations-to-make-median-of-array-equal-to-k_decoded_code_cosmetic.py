class Solution:
    def minOperationsToMakeMedianK(self, arr, k):
        arr.sort()
        length = len(arr)
        mid = length // 2

        currentValue = arr[mid]
        if currentValue == k:
            return 0

        steps = 0
        if currentValue < k:
            while mid < length and arr[mid] < k:
                diff = k - arr[mid]
                steps += diff
                mid += 1
        else:
            while mid >= 0 and arr[mid] > k:
                diff = arr[mid] - k
                steps += diff
                mid -= 1

        return steps