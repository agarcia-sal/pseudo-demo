class Solution:
    def minimumOperations(self, nums, target):
        q = len(nums)
        a = target[0] - nums[0]
        if a < 0:
            a = -a

        def helper(idx, acc):
            if idx >= q:
                return acc
            p = target[idx] - nums[idx]
            s = target[idx - 1] - nums[idx - 1]
            result = acc

            sign_p = 0
            sign_s = 0
            if p > 0:
                sign_p = 1
            elif p < 0:
                sign_p = -1
            if s > 0:
                sign_s = 1
            elif s < 0:
                sign_s = -1

            if sign_p * sign_s > 0:
                diff = 0
                if p < 0:
                    diff = (-p) - abs(s)
                else:
                    diff = p - abs(s)
                if diff < 0:
                    diff = -diff
                if diff > 0:
                    result += diff
            else:
                abs_p = p
                if abs_p < 0:
                    abs_p = -abs_p
                result += abs_p
            return helper(idx + 1, result)

        return helper(1, a)