from typing import List, Optional

class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> Optional[int]:
        nums1.sort()
        nums2.sort()

        n = len(nums1)
        m = len(nums2)
        if m == 0:
            return None  # no nums2 elements to match

        for outer_index in range(n - 1):
            for inner_index in range(outer_index + 1, n - 1):
                filtered_list = []
                # pre-segment: from start to outer_index - 1
                filtered_list.extend(nums1[:outer_index])
                # mid-segment: from outer_index + 1 to inner_index - 1
                filtered_list.extend(nums1[outer_index + 1:inner_index])
                # post-segment: from inner_index + 1 to end
                filtered_list.extend(nums1[inner_index + 1:])

                if len(filtered_list) < m:
                    continue  # filtered_list too short to compare with nums2

                difference = nums2[0] - filtered_list[0]
                valid = True
                for idx in range(m):
                    if idx >= len(filtered_list) or filtered_list[idx] + difference != nums2[idx]:
                        valid = False
                        break

                if valid:
                    return difference

        return None