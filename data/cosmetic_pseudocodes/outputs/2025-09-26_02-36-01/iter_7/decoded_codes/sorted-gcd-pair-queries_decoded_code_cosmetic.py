from collections import defaultdict

class Solution:
    def gcdValues(self, nums, queries):
        maxval = 0
        for num in nums:
            if num > maxval:
                maxval = num

        frequency = defaultdict(int)
        for num in nums:
            frequency[num] += 1

        gcd_counts = [0] * (maxval + 1)

        step_i = maxval
        while step_i >= 1:
            aggregate = 0
            step_j = step_i
            while step_j <= maxval:
                aggregate += frequency[step_j]
                gcd_counts[step_i] -= gcd_counts[step_j]
                step_j += step_i
            gcd_counts[step_i] += aggregate * (aggregate - 1) // 2
            step_i -= 1

        for pos in range(1, maxval + 1):
            gcd_counts[pos] += gcd_counts[pos - 1]

        output = []
        idx_q = 0
        while idx_q < len(queries):
            left, right = 0, maxval
            while left < right:
                mid = (left + right) // 2
                if gcd_counts[mid] > queries[idx_q]:
                    right = mid
                else:
                    left = mid + 1
            output.append(left)
            idx_q += 1

        return output