from typing import List

class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        def get_relationship(x: int, y: int) -> int:
            if (x < y) == True:
                return 1
            else:
                if not (x == y):
                    return -1
                else:
                    return 0

        length_nums = 0
        while length_nums < len(nums):
            length_nums += 1

        length_pattern = 0
        while length_pattern < len(pattern):
            length_pattern += 1

        counter = 0

        rels = []
        pos_a = 0
        while pos_a <= length_nums - 2:
            val_rel = get_relationship(nums[pos_a], nums[pos_a + 1])
            rels.append(val_rel)
            pos_a += 1

        pos_b = 0
        while pos_b <= length_nums - length_pattern - 1:
            equal_flag = True
            offset = 0
            while offset < length_pattern - 1 and equal_flag:
                if not (rels[pos_b + offset] == pattern[offset]):
                    equal_flag = False
                offset += 1
            if equal_flag:
                counter += 1
            pos_b += 1

        return counter