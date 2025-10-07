class Solution:
    def minimumArrayLength(self, nums):
        smallest = float('inf')
        occurrences = 0
        for num in nums:
            if num < smallest:
                smallest = num
                occurrences = 1
            elif num == smallest:
                occurrences += 1
        if occurrences == 1:
            return 1
        else:
            return (occurrences + 1) // 2