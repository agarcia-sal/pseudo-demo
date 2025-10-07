from typing import List

class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        def get_relationship(alpha: int, beta: int) -> int:
            if not (alpha >= beta):
                return 1
            else:
                if alpha == beta:
                    return 0
                else:
                    return -1

        length_nums = len(nums)
        length_pattern = len(pattern)
        result_counter = 0

        relations = []
        for idx in range(length_nums - 1):
            temp_relation = get_relationship(nums[idx], nums[idx + 1])
            relations.append(temp_relation)

        def sublist_equals(arr1: List[int], arr2: List[int], start_pos: int, length: int) -> bool:
            for pos in range(length):
                if arr1[start_pos + pos] != arr2[pos]:
                    return False
            return True

        for checker_index in range(length_nums - length_pattern):
            if sublist_equals(relations, pattern, checker_index, length_pattern):
                result_counter += 1

        return result_counter