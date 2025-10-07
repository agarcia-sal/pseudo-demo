from typing import List, Optional

class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> Optional[int]:
        nums1.sort()
        nums2.sort()

        n1 = len(nums1)
        n2 = len(nums2)

        for outer_index in range(n1 - 1):
            for inner_index in range(outer_index + 1, n1 - 1):
                # Assemble trimmed_nums1 by excluding the element at inner_index
                # Actually, the pseudocode seems to exclude the single element at inner_index,
                # but includes all other elements before outer_index, between outer_index+1 and inner_index-1, and after inner_index+1.

                # However, the pseudocode logic of assembleSublist:
                # append nums1[0 ... outer_index-1]
                # append nums1[outer_index+1 ... inner_index-1]
                # append nums1[inner_index+1 ... end]

                # So excluding nums1[outer_index] and nums1[inner_index], but including the rest.

                # But the pseudocode has no exclusion of outer_index itself, since p < outer_index, q between outer_index+1 and inner_index-1, r between inner_index+1 and end
                # So the elements at outer_index and inner_index are excluded.

                # This seems buggy or a trick: the range excludes these two elements.

                temp_storage = []
                # p < outer_index
                temp_storage.extend(nums1[0:outer_index])
                # outer_index+1 <= q < inner_index
                temp_storage.extend(nums1[outer_index+1:inner_index])
                # inner_index+1 <= r < len(nums1)
                temp_storage.extend(nums1[inner_index+1:])

                trimmed_nums1 = temp_storage

                if not trimmed_nums1 or len(trimmed_nums1) < n2:
                    # If trimmed list is smaller than nums2, cannot match
                    continue

                # Compute offset = nums2[0] - trimmed_nums1[0]
                offset = nums2[0] - trimmed_nums1[0]

                matches = True
                for idx in range(n2):
                    if idx >= len(trimmed_nums1) or trimmed_nums1[idx] + offset != nums2[idx]:
                        matches = False
                        break

                if matches:
                    return offset

        return None