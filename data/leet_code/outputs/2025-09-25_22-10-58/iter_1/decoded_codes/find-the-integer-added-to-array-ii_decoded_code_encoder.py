from typing import List, Optional

class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> Optional[int]:
        nums1.sort()
        nums2.sort()

        n = len(nums1)
        for i in range(n):
            for j in range(i + 1, n):
                # Construct new_nums1 by excluding nums1[i] and nums1[j]
                new_nums1 = nums1[:i] + nums1[i+1:j] + nums1[j+1:]

                if not new_nums1 or len(new_nums1) != len(nums2):
                    # Length must match nums2 to compare sums after adding x
                    continue

                x = nums2[0] - new_nums1[0]
                condition_holds = True
                for k in range(len(nums2)):
                    if new_nums1[k] + x != nums2[k]:
                        condition_holds = False
                        break

                if condition_holds:
                    return x

        return None