class Solution:
    def minOrAfterOperations(self, nums, k):
        def canAchieve(required_or):
            marker = -1
            cnt = 0
            idx = 0
            n = len(nums)
            while idx < n:
                element = nums[idx]
                if marker == -1:
                    marker = element
                else:
                    marker &= element
                if (marker & required_or) == 0:
                    marker = -1
                else:
                    cnt += 1
                    if cnt > k:
                        return False
                idx += 1
            return True

        upper_bound = (1 << 30) - 1
        ans = upper_bound
        counter = 0
        while True:
            if counter > 29:
                break
            bit_filter = 1 << counter
            if (ans & bit_filter) != 0:
                trial_val = ans ^ bit_filter
                inverted_trial = (~trial_val) & upper_bound
                if canAchieve(inverted_trial):
                    ans &= ~bit_filter
            counter += 1
        return ans