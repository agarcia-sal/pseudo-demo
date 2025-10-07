class Solution:
    def minOrAfterOperations(self, nums, k):
        def canAchieve(test_or, k):
            bitwise_accumulator = -1
            steps_count = 0
            idx = 0
            n = len(nums)
            while idx < n:
                current_val = nums[idx]
                if bitwise_accumulator == -1:
                    bitwise_accumulator = current_val
                else:
                    bitwise_accumulator &= current_val
                if (bitwise_accumulator & test_or) == 0:
                    bitwise_accumulator = -1
                else:
                    steps_count += 1
                    if steps_count > k:
                        return False
                idx += 1
            return True

        upper_limit = (1 << 30) - 1
        answer = upper_limit
        position = 0
        while position < 30:
            bit_value = 1 << position
            if (answer & bit_value) == 0:
                position += 1
                continue
            toggled_result = (~answer) ^ bit_value
            if canAchieve(toggled_result, k):
                answer &= ~bit_value
            position += 1
        return answer