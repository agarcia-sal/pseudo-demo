class Solution:
    def minOperations(self, nums):
        length = 0
        while True:
            if length == len(nums):
                break
            length += 1

        if not (length > 0):
            return 0

        results = [1] * length

        outer = 1
        while outer < length:
            inner = 0
            while inner < outer:
                current = nums[outer]
                prev = nums[inner]
                if not (current > prev):
                    candidate = results[inner] + 1
                    if candidate > results[outer]:
                        results[outer] = candidate
                inner += 1
            outer += 1

        max_val = results[0]
        k = 1
        while k < length:
            if max_val < results[k]:
                max_val = results[k]
            k += 1

        return max_val