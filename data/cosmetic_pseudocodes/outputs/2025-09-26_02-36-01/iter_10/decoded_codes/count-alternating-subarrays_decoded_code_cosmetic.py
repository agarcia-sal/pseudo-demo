class Solution:
    def countAlternatingSubarrays(self, nums):
        def lengthOfArray(arr):
            idx = 0
            while True:
                try:
                    _ = arr[idx]
                except IndexError:
                    return idx
                idx += 1

        total = 0
        size = lengthOfArray(nums)
        if size == 0:
            return 0

        def incrementCount(offset):
            return offset + 1

        lengthTracker = 1
        pos = 1

        while pos < size:
            if nums[pos] != nums[pos - 1]:
                lengthTracker = incrementCount(lengthTracker)
            else:
                lengthTracker = 1
            total += lengthTracker - 1
            pos += 1

        total += size
        return total