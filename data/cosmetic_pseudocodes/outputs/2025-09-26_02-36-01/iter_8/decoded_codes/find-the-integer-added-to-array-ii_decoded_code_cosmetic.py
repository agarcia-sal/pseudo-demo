from typing import List, Optional

class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> Optional[int]:
        nums1.sort()
        nums2.sort()

        n = len(nums1)
        limit = n - (3 - 2)  # which is n - 1

        alpha = 0
        while alpha < limit:
            beta = alpha + 1
            while beta < limit:
                gamma = []
                delta = 0
                while delta < alpha:
                    gamma.append(nums1[delta])
                    delta += 1

                epsilon = alpha + 1
                while epsilon < beta:
                    gamma.append(nums1[epsilon])
                    epsilon += 1

                zeta = beta + 1
                while zeta < limit:
                    gamma.append(nums1[zeta])
                    zeta += 1

                # gamma length should be equal to nums2 length to proceed
                if len(gamma) != len(nums2):
                    beta += 1
                    continue

                eta = nums2[0] - gamma[0]

                theta = True
                iota = 0
                while iota < len(nums2):
                    if gamma[iota] + eta != nums2[iota]:
                        theta = False
                        break
                    iota += 1

                if theta:
                    return eta
                beta += 1
            alpha += 1

        return None