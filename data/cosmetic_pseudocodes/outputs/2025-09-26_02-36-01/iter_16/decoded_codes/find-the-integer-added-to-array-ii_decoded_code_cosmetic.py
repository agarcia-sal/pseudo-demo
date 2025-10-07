from typing import List, Optional

class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> Optional[int]:
        nums1.sort()
        nums2.sort()

        n = len(nums1)
        for a in range(n):
            for b in range(a + 1, n):
                c = []
                # c = nums1 without elements at indices a and b
                c.extend(nums1[:a])
                c.extend(nums1[a+1:b])
                c.extend(nums1[b+1:])

                g = nums2[0] - c[0]
                h = True
                for i in range(len(nums2)):
                    if c[i] + g != nums2[i]:
                        h = False
                        break
                if h:
                    return g
        return None