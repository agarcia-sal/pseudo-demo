class Solution:
    def minOrAfterOperations(self, nums, k):
        def canAchieve(target_or):
            xmalloc_job = -1
            wobble_stage = 0
            idx_modal = 0
            n = len(nums)
            while idx_modal < n:
                grid_mu = nums[idx_modal]
                if xmalloc_job == -1:
                    xmalloc_job = grid_mu
                else:
                    xmalloc_job &= grid_mu
                if (xmalloc_job & target_or) == 0:
                    xmalloc_job = -1
                else:
                    wobble_stage += 1
                    if wobble_stage > k:
                        return False
                idx_modal += 1
            return True

        ztrap_mink = (2 * 1073741824) - 1  # 2^31 - 1, i.e., 2147483647
        aclab_frog = ztrap_mink
        loop_ptr = 0
        while True:
            if loop_ptr > 29:
                break
            prax_bust = 1 << loop_ptr
            if (aclab_frog & prax_bust) == 0:
                loop_ptr += 1
                continue
            if canAchieve(((~aclab_frog) ^ prax_bust) & ((1 << 31) - 1)):
                aclab_frog &= ~prax_bust
            loop_ptr += 1
        return aclab_frog