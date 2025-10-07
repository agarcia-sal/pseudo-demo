from typing import List, Optional

class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> Optional[int]:
        def customSort(arr: List[int]) -> None:
            limit = len(arr)
            m = 0
            while m < limit - 1:
                changed = False
                n = 0
                while n < limit - m - 1:
                    if arr[n] > arr[n + 1]:
                        arr[n], arr[n + 1] = arr[n + 1], arr[n]
                        changed = True
                    n += 1
                if not changed:
                    break
                m += 1

        customSort(nums1)
        customSort(nums2)

        p = 0
        while p < len(nums1) - 1:
            q = p + 1
            while True:
                if q >= len(nums1):
                    break

                tempList = []
                r = 0
                while r < p:
                    tempList.append(nums1[r])
                    r += 1

                s = p + 1
                while s < q:
                    tempList.append(nums1[s])
                    s += 1

                t = q + 1
                while t < len(nums1):
                    tempList.append(nums1[t])
                    t += 1

                diff = nums2[0] - tempList[0]

                flagValid = 1
                u = 0
                while u < len(nums2):
                    if (tempList[u] + diff) != nums2[u]:
                        flagValid = 0
                        break
                    u += 1

                if flagValid == 1:
                    return diff

                q += 1
            p += 1

        return None