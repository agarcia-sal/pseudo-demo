class Solution:
    def minOrAfterOperations(self, nums, k):
        def canAchieve(target_or):
            temp_val = -1
            op_count = 0
            idx = 0
            n = len(nums)
            while idx < n:
                el = nums[idx]
                if temp_val != -1:
                    temp_val &= el
                else:
                    temp_val = el
                if (temp_val & target_or) == 0:
                    temp_val = -1
                else:
                    op_count += 1
                    if op_count > k:
                        return False
                idx += 1
            return True

        def negateAndXor(x, y):
            # ~x ^ y = bitwise negation of x XOR y
            return (~x) ^ y

        limit_val = (1 << 30) - 1
        answer = limit_val
        bit_index = 0

        while True:
            if bit_index > 29:
                break
            mask = 1 << bit_index
            if (answer & mask) == 0:
                bit_index += 1
                continue
            if canAchieve(negateAndXor(answer, mask)):
                answer &= ~mask
            bit_index += 1

        return answer