class Solution:
    def maxOperations(self, nums):
        def explore(left, right, target, cache):
            if left >= right:
                return 0
            key = (left, right, target)
            if key in cache:
                return cache[key]

            best = 0
            if left + 1 < len(nums):
                sumLeftPair = nums[left] + nums[left + 1]
                if sumLeftPair == target:
                    best = max(best, 1 + explore(left + 2, right, target, cache))
            if right - 1 >= 0:
                sumRightPair = nums[right] + nums[right - 1]
                if sumRightPair == target:
                    best = max(best, 1 + explore(left, right - 2, target, cache))
            sumOuterPair = nums[left] + nums[right]
            if sumOuterPair == target:
                best = max(best, 1 + explore(left + 1, right - 1, target, cache))

            cache[key] = best
            return best

        total_len = len(nums)
        if total_len < 2:
            return 0

        option1 = 1 + explore(2, total_len - 1, nums[0] + nums[1], {}) if total_len > 2 else 0
        option2 = 1 + explore(0, total_len - 3, nums[total_len - 1] + nums[total_len - 2], {}) if total_len > 2 else 0
        option3 = 1 + explore(1, total_len - 2, nums[0] + nums[total_len - 1], {}) if total_len > 2 else 0

        return max(option1, option2, option3)