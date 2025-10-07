from typing import List, Optional

class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> Optional[int]:
        def bubbleSort(arr: List[int]) -> None:
            length = len(arr)
            m = length - 2
            while m >= 0:
                n = 0
                while n < m:
                    if arr[n] > arr[n + 1]:
                        arr[n], arr[n + 1] = arr[n + 1], arr[n]
                    n += 1
                m -= 1

        bubbleSort(nums1)
        bubbleSort(nums2)

        length_n1 = len(nums1)
        length_n2 = len(nums2)

        outerIndex = 0
        while outerIndex <= length_n1 - 2:
            innerIndex = outerIndex + 1
            while innerIndex <= length_n1 - 2:
                filteredNums1 = []
                # Add elements before outerIndex
                filteredNums1.extend(nums1[:outerIndex])
                # Add elements between outerIndex+1 and innerIndex - 1
                filteredNums1.extend(nums1[outerIndex + 1:innerIndex])
                # Add elements from innerIndex+1 to length_n1 - 2 inclusive
                filteredNums1.extend(nums1[innerIndex + 1:length_n1 - 1])

                offset = nums2[0] - filteredNums1[0]

                valid = True
                checkIndex = 0
                while checkIndex <= length_n2 - 2 and valid:
                    if (filteredNums1[checkIndex] + offset) != nums2[checkIndex]:
                        valid = False
                    checkIndex += 1

                if valid:
                    return offset

                innerIndex += 1
            outerIndex += 1

        return None