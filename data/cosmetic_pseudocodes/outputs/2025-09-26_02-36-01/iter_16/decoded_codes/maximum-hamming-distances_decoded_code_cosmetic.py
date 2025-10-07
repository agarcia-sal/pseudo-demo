class Solution:
    def maxHammingDistances(self, nums: list[int], m: int) -> list[int]:
        alpha = []
        beta = 0
        while beta < len(nums):
            gamma = ""
            delta = 0
            # Pad with leading zeros until length equals m
            while len(bin(nums[beta])[2:]) + delta < m:
                gamma = "0" + gamma
                delta += 1
            epsilon = bin(nums[beta])[2:]
            zeta = gamma + epsilon
            alpha.append(zeta)
            beta += 1

        def hamming_distance(bin1: str, bin2: str) -> int:
            theta = 0
            i = 0
            while i < len(bin1):
                if bin1[i] != bin2[i]:
                    theta += 1
                i += 1
            return theta

        eta = []
        i1 = 0
        while i1 < len(nums):
            max_dist_i = 0
            i2 = 0
            while i2 < len(nums):
                if i1 != i2:
                    dist_i = hamming_distance(alpha[i1], alpha[i2])
                    if dist_i > max_dist_i:
                        max_dist_i = dist_i
                i2 += 1
            eta.append(max_dist_i)
            i1 += 1

        return eta