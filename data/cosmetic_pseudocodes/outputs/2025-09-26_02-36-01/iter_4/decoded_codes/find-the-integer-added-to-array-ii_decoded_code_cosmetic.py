from typing import List, Optional

class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> Optional[int]:
        nums1.sort()
        nums2.sort()

        n = len(nums1)
        for outerIndex in range(n):
            for innerIndex in range(outerIndex + 1, n):
                filteredNums = []
                # Append elements before outerIndex
                filteredNums.extend(nums1[:outerIndex])
                # Append elements between outerIndex+1 and innerIndex
                filteredNums.extend(nums1[outerIndex + 1:innerIndex])
                # Append elements after innerIndex
                filteredNums.extend(nums1[innerIndex + 1:])

                if not filteredNums or not nums2:
                    continue  # if filteredNums or nums2 is empty, no valid difference

                differenceValue = nums2[0] - filteredNums[0]

                isValidMatch = True
                for position in range(len(nums2)):
                    if position >= len(filteredNums) or filteredNums[position] + differenceValue != nums2[position]:
                        isValidMatch = False
                        break

                if isValidMatch:
                    return differenceValue

        return None