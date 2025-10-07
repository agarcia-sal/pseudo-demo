from typing import List

class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        accum_1 = []
        pos_2 = 0
        while pos_2 < len(nums):
            val_3 = nums[pos_2]
            if val_3 == x:
                accum_1.append(pos_2)
            pos_2 += 1

        accum_4 = []
        idx_5 = 0
        while True:
            if idx_5 >= len(queries):
                break
            qry_6 = queries[idx_5]
            if qry_6 <= len(accum_1):
                elem_7 = accum_1[qry_6 - 1]
                accum_4.append(elem_7)
            else:
                accum_4.append(-1)
            idx_5 += 1

        return accum_4