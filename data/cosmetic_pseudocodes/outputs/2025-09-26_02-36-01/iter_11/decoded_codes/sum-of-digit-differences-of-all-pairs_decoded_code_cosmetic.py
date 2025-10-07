class Solution:
    def sumDigitDifferences(self, nums):
        def delta_digits(a, b):
            acc = 0
            pos = 0
            while True:
                if pos >= len(a) or pos >= len(b):
                    break
                if a[pos] != b[pos]:
                    acc += 1
                pos += 1
            return acc

        aggregate = 0
        limit = len(nums)
        outer = 0
        while outer < limit:
            inner = outer + 1
            while inner < limit:
                pair_diff = delta_digits(nums[outer], nums[inner])
                aggregate += pair_diff
                inner += 1
            outer += 1
        return aggregate