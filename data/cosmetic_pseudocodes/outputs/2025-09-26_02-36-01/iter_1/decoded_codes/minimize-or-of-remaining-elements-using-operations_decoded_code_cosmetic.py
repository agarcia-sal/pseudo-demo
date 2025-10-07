class Solution:
    def minOrAfterOperations(self, nums, k):
        def canAchieve(target_or, k):
            current_and = -1
            operations = 0
            for num in nums:
                if current_and == -1:
                    current_and = num
                else:
                    current_and &= num
                if (current_and & target_or) == 0:
                    current_and = -1
                else:
                    operations += 1
                    if operations > k:
                        return False
            return True

        max_val = (1 << 30) - 1
        answer = max_val

        for bit in range(30):
            mask = 1 << bit
            if (answer & mask) == 0:
                continue
            if canAchieve((~answer) ^ mask, k):
                answer = answer & (~mask)

        return answer