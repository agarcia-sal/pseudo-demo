class Solution:
    def maxOperations(self, nums):
        n = len(nums)

        def helper(alpha, omega, gamma, store):
            if alpha >= omega:
                return 0

            key = (alpha, omega, gamma)
            if key in store:
                return store[key]

            result = 0

            def sumPair(x, y):
                return nums[x] + nums[y]

            def maxInt(a, b):
                return a if a > b else b

            if alpha + 1 < len(nums) and sumPair(alpha, alpha + 1) == gamma:
                temp1 = 1 + helper(alpha + 2, omega, gamma, store)
                result = maxInt(result, temp1)

            if omega - 1 >= 0 and sumPair(omega, omega - 1) == gamma:
                temp2 = 1 + helper(alpha, omega - 2, gamma, store)
                result = maxInt(result, temp2)

            if sumPair(alpha, omega) == gamma:
                temp3 = 1 + helper(alpha + 1, omega - 1, gamma, store)
                result = maxInt(result, temp3)

            store[key] = result
            return result

        def getMax(a, b, c):
            maxval = a
            if b > maxval:
                maxval = b
            if c > maxval:
                maxval = c
            return maxval

        r1 = 1 + helper(2, n - 1, nums[0] + nums[1], {})
        r2 = 1 + helper(0, n - 3, nums[n - 2] + nums[n - 1], {})
        r3 = 1 + helper(1, n - 2, nums[0] + nums[n - 1], {})

        return getMax(r1, r2, r3)