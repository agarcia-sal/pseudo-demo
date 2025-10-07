from typing import List, Optional

class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> Optional[int]:
        def arrange(seq: List[int]) -> None:
            d = len(seq)
            b = 1
            while b < d:
                a = 0
                while a < d - b:
                    if seq[a] > seq[a + 1]:
                        seq[a], seq[a + 1] = seq[a + 1], seq[a]
                    a += 1
                b += 1

        arrange(nums1)
        arrange(nums2)

        p = 0
        while p < len(nums1) - 1:
            q = p + 1
            while q < len(nums1):
                v = []
                # append nums1[:p]
                v.extend(nums1[:p])
                # append nums1[p+1:q]
                v.extend(nums1[p+1:q])
                # append nums1[q+1:]
                v.extend(nums1[q+1:])

                delta = nums2[0] - v[0]
                satisfied = True
                for z in range(len(nums2)):
                    if v[z] + delta != nums2[z]:
                        satisfied = False
                        break

                if satisfied:
                    return delta
                q += 1
            p += 1
        return None