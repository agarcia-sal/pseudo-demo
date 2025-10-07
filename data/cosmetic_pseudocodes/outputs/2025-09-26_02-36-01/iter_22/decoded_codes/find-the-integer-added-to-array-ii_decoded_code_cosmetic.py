from typing import List, Optional

class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> Optional[int]:
        nums1.sort()
        nums2.sort()

        n1 = len(nums1)
        n2 = len(nums2)

        for a in range(n1 - 1):
            for b in range(a + 1, n1):
                # Construct tempList by excluding nums1[a] and nums1[b]
                tempList = nums1[:a] + nums1[a+1:b] + nums1[b+1:]
                if not tempList or len(tempList) != n2:
                    continue
                diff = nums2[0] - tempList[0]
                valid = True
                for f in range(n2):
                    if tempList[f] + diff != nums2[f]:
                        valid = False
                        break
                if valid:
                    return diff
        return None