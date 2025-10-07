from typing import List, Optional

class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> Optional[int]:
        nums1.sort()
        nums2.sort()

        for start_index in range(len(nums1) - 1):
            for end_index in range(start_index + 1, len(nums1)):
                filtered_nums1 = [nums1[i] for i in range(len(nums1)) if i != start_index and i != end_index]

                # If filtered_nums1 and nums2 lengths differ, skip
                if len(filtered_nums1) != len(nums2):
                    continue

                offset = nums2[0] - filtered_nums1[0]

                is_match = True
                for pos in range(len(nums2)):
                    if filtered_nums1[pos] + offset != nums2[pos]:
                        is_match = False
                        break

                if is_match:
                    return offset

        return None