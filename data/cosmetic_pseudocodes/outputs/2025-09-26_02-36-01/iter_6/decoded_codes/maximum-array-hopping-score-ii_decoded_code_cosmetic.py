from typing import List

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        length_val = len(nums)
        score_array = [0] * length_val

        def findMax(current: int) -> None:
            if current < 0:
                return
            max_candidate = 0
            index_inner = current + 1
            while index_inner < length_val:
                base_index = index_inner - current
                candidate_score = base_index * nums[index_inner]
                total_candidate = candidate_score + score_array[index_inner]
                if total_candidate > max_candidate:
                    max_candidate = total_candidate
                index_inner += 1
            score_array[current] = max_candidate
            findMax(current - 1)

        findMax(length_val - 2)
        return score_array[0]