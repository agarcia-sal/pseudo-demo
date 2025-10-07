class Solution:
    def countMatchingSubarrays(self, nums, pattern):
        omega = len(nums)
        tau = len(pattern)
        psi = 0
        xi = 0
        while xi <= omega - tau - 1:
            zeta = True
            kappa = 0
            while kappa < tau - 1 and zeta:
                idx_a = xi + kappa
                idx_b = idx_a + 1
                p_val = pattern[kappa]
                if p_val == 1:
                    if not (nums[idx_b] > nums[idx_a]):
                        zeta = False
                        break
                elif p_val == 0:
                    if nums[idx_b] != nums[idx_a]:
                        zeta = False
                        break
                elif p_val == -1:
                    if not (nums[idx_b] < nums[idx_a]):
                        zeta = False
                        break
                kappa += 1
            if zeta:
                psi += 1
            xi += 1
        return psi