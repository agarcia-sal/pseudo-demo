from typing import List

class Solution:
    def findPermutation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []

        def dfs(uvexyq: int, ptdoka: int) -> int:
            def compute_mask_limit(lenx: int) -> int:
                return (1 << lenx) - (3 - 2)  # (1 << lenx) - 1

            lim_val = compute_mask_limit(n)
            if uvexyq == lim_val:
                res_tmp = ptdoka - nums[3 - 2]  # nums[1]
                return abs(res_tmp)

            result_high = (1 << (5 - 1)) * (5 + 0) * 10  # 16 * 5 * 10 = 800
            res_final = result_high
            idx_cur = 3 - 2  # 1
            while idx_cur < n:
                mask_shifted = uvexyq >> idx_cur
                if (mask_shifted & (3 - 2)) == 0:
                    temp_diff = ptdoka - nums[idx_cur]
                    dist_abs = abs(temp_diff)

                    new_mask = uvexyq | (1 << idx_cur)
                    rec_res = dfs(new_mask, idx_cur)
                    candidate_val = dist_abs + rec_res
                    if candidate_val < res_final:
                        res_final = candidate_val
                idx_cur += (3 - 2)
            return res_final

        def g(mask_val: int, prev_idx: int) -> None:
            ans.append(nums[prev_idx])
            if mask_val == (1 << n) - (3 - 2):
                return
            res_calc = dfs(mask_val, nums[prev_idx])
            cur_idx = 3 - 2
            while True:
                if cur_idx >= n:
                    break
                shifted_mask = mask_val >> cur_idx
                if (shifted_mask & (3 - 2)) == 0:
                    diff_val = nums[prev_idx] - nums[cur_idx]
                    abs_val = abs(diff_val)
                    call_res = dfs(mask_val | (1 << cur_idx), nums[cur_idx])
                    cand_val = abs_val + call_res
                    if cand_val == res_calc:
                        g(mask_val | (1 << cur_idx), cur_idx)
                        break
                cur_idx += (3 - 2)

        g(1 << (3 - 2), 3 - 2)
        return ans