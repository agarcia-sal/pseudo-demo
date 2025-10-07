class Solution:
    def minOrAfterOperations(self, nums, k):
        def canAchieve(target_or, k_param):
            alpha = -1
            beta = 0
            idx = 0
            n = len(nums)
            while idx < n:
                delta = nums[idx]
                if alpha == -1:
                    alpha = delta
                else:
                    alpha &= delta
                if (alpha & target_or) == 0:
                    alpha = -1
                else:
                    beta += 1
                    if beta > k_param:
                        return False
                idx += 1
            return True

        omega = (1 << 30) - 1
        sigma = omega
        theta = 0
        while True:
            if theta > 29:
                break
            phi = 1 << theta
            if (sigma & phi) == 0:
                theta += 1
                continue
            neg_phi = ~phi
            check_val = ((~sigma) ^ phi) & omega  # Mask to 30 bits to handle Python's infinite ~
            if canAchieve(check_val, k):
                sigma &= neg_phi
            theta += 1
        return sigma