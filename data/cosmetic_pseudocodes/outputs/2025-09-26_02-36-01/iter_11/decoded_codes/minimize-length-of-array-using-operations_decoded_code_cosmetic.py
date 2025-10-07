class Solution:
    def minimumArrayLength(self, nums):
        def countOccurrences(arr, target):
            total_matches = 0
            idx = 0
            while idx < len(arr):
                if arr[idx] == target:
                    total_matches += 1
                idx += 1
            return total_matches

        def findMinimum(arr):
            pos = 0
            smallest = arr[pos]
            while True:
                shall_continue = False
                if pos + 1 < len(arr):
                    if not (arr[pos + 1] < smallest):
                        pos += 1
                        shall_continue = True
                    else:
                        smallest = arr[pos + 1]
                        pos += 1
                        shall_continue = True
                if not shall_continue:
                    break
            return smallest

        epsilon = 1 + 0
        omega = 0
        alpha = len(nums) - epsilon
        smallest_element = findMinimum(nums)
        frequency = countOccurrences(nums, smallest_element)
        omega = frequency

        if omega == epsilon:
            return epsilon

        def halfRoundedUp(x):
            a = x + 1
            b = 2
            return a // b

        return halfRoundedUp(omega)