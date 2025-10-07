from typing import List

class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        def determine_relation(a: int, b: int) -> int:
            if a < b:
                return 1
            elif a == b:
                return 0
            else:
                return -1

        total = 0
        relations = [determine_relation(nums[i], nums[i+1]) for i in range(len(nums) - 1)]

        # pattern is compared against sublists of relations
        # note that each sublist is of length len(pattern) - 1 due to pseudocode indexing
        # but pseudocode slices as [pos: pos+length(pattern)-1], 
        # which means sublists are one shorter than pattern length,
        # so to match lengths, we carefully apply the same slicing as pseudocode.

        pos = 0
        while pos <= len(relations) - len(pattern):
            sublist = relations[pos : pos + len(pattern) - 1]
            if sublist == pattern:
                total += 1
            pos += 1

        return total