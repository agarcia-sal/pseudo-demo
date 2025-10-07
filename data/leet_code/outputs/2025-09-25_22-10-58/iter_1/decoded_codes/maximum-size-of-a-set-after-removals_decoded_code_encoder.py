from typing import List

class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        half_n = n // 2

        set1 = set(nums1)
        set2 = set(nums2)

        common = set1 & set2
        unique1 = set1 - common
        unique2 = set2 - common

        take_from_unique1 = min(half_n, len(unique1))
        take_from_unique2 = min(half_n, len(unique2))

        take_from_common = max(0, half_n - take_from_unique1) + max(0, half_n - take_from_unique2)

        total_elements = take_from_unique1 + take_from_unique2 + min(take_from_common, len(common))

        return total_elements