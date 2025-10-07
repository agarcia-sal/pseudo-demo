class Solution:
    def minOrAfterOperations(self, nums, k):
        def canAchieve(target_or):
            state_tmp = -1
            count_ops = 0
            idx = 0
            n = len(nums)
            while idx < n:
                el = nums[idx]
                if state_tmp == -1:
                    state_tmp = el
                else:
                    state_tmp &= el
                if (state_tmp & target_or) == 0:
                    state_tmp = -1
                else:
                    count_ops += 1
                    if count_ops > k:
                        return False
                idx += 1
            return True

        upper_bound = (1 << 30) - 1
        answer = upper_bound
        bit_counter = 0
        while True:
            if bit_counter > 29:
                break
            flag_mask = 1 << bit_counter
            if (answer & flag_mask) == 0:
                bit_counter += 1
                continue
            complement = ~(answer ^ flag_mask)
            # limit complement to 30 bits only
            complement &= upper_bound
            if canAchieve(complement):
                answer &= complement
            bit_counter += 1
        return answer