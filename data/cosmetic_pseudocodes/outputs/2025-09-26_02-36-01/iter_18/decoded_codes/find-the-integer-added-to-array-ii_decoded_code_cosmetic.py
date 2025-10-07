from typing import List, Optional

class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> Optional[int]:
        nums1.sort()
        nums2.sort()

        n = len(nums1)
        m = len(nums2)

        for alpha in range(n - 1):
            for beta in range(alpha + 1, n):
                # Construct gamma by excluding nums1[alpha] and nums1[beta]
                gamma = nums1[:alpha] + nums1[alpha+1:beta] + nums1[beta+1:]

                # If lengths differ, no need to check this gamma
                if len(gamma) != m:
                    continue

                eta = nums2[0] - gamma[0]

                theta = True
                for iota in range(m):
                    if gamma[iota] + eta != nums2[iota]:
                        theta = False
                        break

                if theta:
                    return eta

        return None