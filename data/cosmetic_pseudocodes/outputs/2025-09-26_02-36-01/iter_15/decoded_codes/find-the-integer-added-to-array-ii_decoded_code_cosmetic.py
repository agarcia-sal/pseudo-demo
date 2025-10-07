from typing import List, Optional

class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> Optional[int]:
        nums1.sort()
        nums2.sort()

        n = len(nums1)
        for alpha in range(n):
            for beta in range(alpha + 1, n):
                gamma = []
                # Add elements before alpha
                gamma.extend(nums1[:alpha])
                # Add elements between alpha and beta
                gamma.extend(nums1[alpha + 1:beta])
                # Add elements after beta
                gamma.extend(nums1[beta + 1:])

                if not gamma:
                    continue  # Avoid index errors if gamma is empty

                eta = nums2[0] - gamma[0]

                # Check if adding eta to gamma equals nums2
                if all((gamma[i] + eta) == nums2[i] for i in range(len(nums2))):
                    return eta

        return None