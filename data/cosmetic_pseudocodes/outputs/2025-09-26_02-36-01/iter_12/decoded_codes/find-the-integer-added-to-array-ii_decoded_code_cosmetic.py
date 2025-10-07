from typing import List, Optional

class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> Optional[int]:
        def ascSort(arr: List[int]) -> None:
            idx1 = 0
            n = len(arr)
            while idx1 < n - 1:
                idx2 = 0
                while idx2 < n - 1 - idx1:
                    if arr[idx2] > arr[idx2 + 1]:
                        arr[idx2], arr[idx2 + 1] = arr[idx2 + 1], arr[idx2]
                    idx2 += 1
                idx1 += 1

        def append_to_list(lst: List[int], val: int) -> None:
            lst.append(val)

        ascSort(nums1)
        ascSort(nums2)

        n = len(nums1)
        if n == 0 or len(nums2) == 0:
            return None

        a = 0
        while a < n - 1:
            b = a + 1
            while b < n:
                newList = []

                idx = 0
                # copy until a (excluding a)
                while idx < a:
                    append_to_list(newList, nums1[idx])
                    idx += 1

                # copy between a and b (including a and b)
                while idx < b:
                    append_to_list(newList, nums1[idx])
                    idx += 1

                # copy after b
                while idx < n:
                    append_to_list(newList, nums1[idx])
                    idx += 1

                # Adjust for the indexing in pseudocode: idx goes from 0 to a-1 in copy_until_a,
                # then idx is set to a+1 but pseudocode includes nums1[a] and nums1[b] in copy_between_a_b.
                # However in pseudocode, 
                # copy_until_a stops when idx < a is false, then idx := a+1,
                # copy_between_a_b copies when idx < b.
                # It's possible the pseudocode is skipping nums1[a].
                # To strictly follow pseudocode, rewrite precise copy loops:

                # Reimplement newList following pseudocode exactly:

            a += 1  # Just increment here, will reimplement inner logic below

        # Since pseudocode has a complex copying strategy, carefully translate it verbatim below:

        a = 0
        while a < n - 1:
            b = a + 1
            while b < n:
                newList = []

                # copy_until_a: idx from 0 to a-1
                idx = 0
                while idx < a:
                    append_to_list(newList, nums1[idx])
                    idx += 1

                # copy_between_a_b: idx from a to b-1
                while idx < b:
                    append_to_list(newList, nums1[idx])
                    idx += 1

                # copy_after_b: idx from b to end
                while idx < n:
                    append_to_list(newList, nums1[idx])
                    idx += 1

                # Note: The pseudocode sets idx := a + 1 after copy_until_a label, so it omits nums1[a],
                # but then copy_between_a_b copies from idx to b - 1.
                # This logic would skip nums1[a], thus not exactly matching pseudocode.
                # To match pseudocode exactly, follow the labels and idx assignments precisely:

                # Let's implement exactly as pseudocode assigns idx:

                # copy_until_a:
                #   if idx < a: append nums1[idx]; idx++
                #   else idx := a + 1

                # copy_between_a_b:
                #   if idx < b: append nums1[idx]; idx++
                #   else idx := b + 1

                # copy_after_b:
                #   if idx < len(nums1): append nums1[idx]; idx++

                # Re-implement newList for each (a,b) based on pseudocode:

                # Step 1: copy_until_a
                newList = []
                idx = 0
                while True:
                    if not (idx < a):
                        idx = a + 1
                        break
                    append_to_list(newList, nums1[idx])
                    idx += 1
                # Step 2: copy_between_a_b
                while True:
                    if not (idx < b):
                        idx = b + 1
                        break
                    append_to_list(newList, nums1[idx])
                    idx += 1
                # Step 3: copy_after_b
                while idx < n:
                    append_to_list(newList, nums1[idx])
                    idx += 1

                # After construction, newList length might be less than nums2 length or vice versa
                if len(newList) != len(nums2):
                    b += 1
                    continue

                offset = nums2[0] - newList[0]

                conditionFlag = True
                cnt = 0
                while cnt < len(nums2):
                    if newList[cnt] + offset != nums2[cnt]:
                        conditionFlag = False
                        break
                    cnt += 1

                if conditionFlag:
                    return offset

                b += 1
            a += 1

        return None