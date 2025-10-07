from typing import List, Optional

class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> Optional[int]:
        nums1.sort()
        nums2.sort()

        n = len(nums1)
        m = len(nums2)

        # Iterate over all pairs (a, b) to remove nums1[a] and nums1[b]
        for a in range(n - 1):
            for b in range(a + 1, n):
                # Construct tempList by removing nums1[a] and nums1[b]
                tempList = nums1[:a] + nums1[a+1:b] + nums1[b+1:]
                if len(tempList) != len(nums2):
                    # Length must match to compare
                    continue
                # Calculate the offset to match start of nums2
                offset = nums2[0] - tempList[0]

                # Check if adding offset to tempList yields nums2
                valid = True
                for f in range(m):
                    if tempList[f] + offset != nums2[f]:
                        valid = False
                        break
                if valid:
                    return offset

        return None