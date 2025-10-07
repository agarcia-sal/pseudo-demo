from typing import List

class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        def helper_check(k: int) -> bool:
            latest_pos = [-1] * len(nums)
            idx = 0
            while idx < k:
                pos = changeIndices[idx] - 1
                latest_pos[pos] = idx
                idx += 1

            needed = sum(nums)
            posc = 0
            marked = set()
            iter_ = 0
            while iter_ < k:
                current_pos = changeIndices[iter_] - 1
                if current_pos not in marked:
                    if latest_pos[current_pos] == iter_:
                        if nums[current_pos] <= posc:
                            posc -= nums[current_pos]
                            marked.add(current_pos)
                        else:
                            return False
                    else:
                        posc += 1
                else:
                    posc += 1
                iter_ += 1

            return len(marked) == len(nums)

        left_bound = 0
        right_bound = len(changeIndices) + 1
        answer = -1
        while left_bound < right_bound:
            middle = (left_bound + right_bound) // 2
            if helper_check(middle):
                right_bound = middle
            else:
                left_bound += 1

        if left_bound <= len(changeIndices):
            answer = left_bound
        else:
            answer = -1

        return answer