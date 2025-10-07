from typing import List

class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        total_count = len(nums1)
        half_limit = total_count // 2

        distinct1 = set(nums1)
        distinct2 = set(nums2)

        common_elements = distinct1.intersection(distinct2)
        exclusive1 = distinct1 - common_elements
        exclusive2 = distinct2 - common_elements

        pick_from_exclusive1 = min(len(exclusive1), half_limit)
        pick_from_exclusive2 = min(len(exclusive2), half_limit)

        leftover1 = half_limit - pick_from_exclusive1
        leftover2 = half_limit - pick_from_exclusive2

        pick_from_common = leftover1 + leftover2
        pick_from_common = min(pick_from_common, len(common_elements))

        answer = pick_from_exclusive1 + pick_from_exclusive2 + pick_from_common
        return answer