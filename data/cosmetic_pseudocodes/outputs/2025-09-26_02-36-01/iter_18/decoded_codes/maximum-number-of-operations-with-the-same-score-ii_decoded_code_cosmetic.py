class Solution:
    def maxOperations(self, nums):
        def recur(a, b, c, d):
            if a >= b:
                return 0
            key = (a, b, c)
            if key in d:
                return d[key]
            result = 0
            if nums[a] + nums[a + 1] == c:
                temp1 = 1 + recur(a + 2, b, c, d)
                if temp1 > result:
                    result = temp1
            if nums[b] + nums[b - 1] == c:
                temp2 = 1 + recur(a, b - 2, c, d)
                if temp2 > result:
                    result = temp2
            if nums[a] + nums[b] == c:
                temp3 = 1 + recur(a + 1, b - 1, c, d)
                if temp3 > result:
                    result = temp3
            d[key] = result
            return result

        val1 = 1 + recur(2, len(nums) - 1, nums[0] + nums[1], {})
        val2 = 1 + recur(0, len(nums) - 3, nums[-1] + nums[-2], {})
        val3 = 1 + recur(1, len(nums) - 2, nums[0] + nums[-1], {})
        return max(val1, val2, val3)