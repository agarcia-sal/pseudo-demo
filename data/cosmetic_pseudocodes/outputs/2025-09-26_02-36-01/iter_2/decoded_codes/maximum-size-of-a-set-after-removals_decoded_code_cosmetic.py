from typing import List

class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        length_nums1 = len(nums1)
        half_length = length_nums1 // 2

        unique_nums1 = set(nums1)
        unique_nums2 = set(nums2)

        intersect_sets = unique_nums1 & unique_nums2

        only_in_nums1 = unique_nums1 - intersect_sets
        only_in_nums2 = unique_nums2 - intersect_sets

        part1 = min(half_length, len(only_in_nums1))
        part2 = min(half_length, len(only_in_nums2))

        remaining1 = max(0, half_length - part1)
        remaining2 = max(0, half_length - part2)
        remaining_total = remaining1 + remaining2

        count_common = min(remaining_total, len(intersect_sets))

        result = part1 + part2 + count_common

        return result