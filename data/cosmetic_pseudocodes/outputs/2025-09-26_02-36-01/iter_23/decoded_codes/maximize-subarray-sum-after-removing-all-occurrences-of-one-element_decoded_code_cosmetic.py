class Solution:
    def maxSubarraySum(self, nums):
        def kadane(arr):
            u1 = arr[0]
            u2 = arr[0]

            def kadane_loop(index):
                if index >= len(arr):
                    return u2
                v1 = arr[index]
                nonlocal u1, u2

                if v1 > u1 + v1:
                    u1 = v1
                else:
                    u1 = u1 + v1

                if u2 < u1:
                    u2 = u1

                return kadane_loop(index + 1)

            return kadane_loop(1)

        z1 = kadane(nums)
        z2 = set()
        for v2 in nums:
            if v2 not in z2:
                z2.add(v2)

        z2 = list(z2)

        def process_unique(index):
            if index >= len(z2):
                return z1
            k = z2[index]
            w = []

            def filter_loop(j):
                if j >= len(nums):
                    return
                e = nums[j]
                if e != k:
                    w.append(e)
                filter_loop(j + 1)

            filter_loop(0)

            nonlocal z1
            if w:
                z3 = kadane(w)
                if z1 < z3:
                    z1 = z3

            return process_unique(index + 1)

        return process_unique(0)