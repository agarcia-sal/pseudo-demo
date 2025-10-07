from typing import List, Optional

class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> Optional[int]:
        nums1.sort()
        nums2.sort()

        m = len(nums1)
        n = len(nums2)

        def check_adjusted(subset: List[int], adjustment: int) -> bool:
            # Recursive check if each element in subset plus adjustment matches nums2
            def loop_check(p: int) -> bool:
                if p == n:
                    return True
                if subset[p] + adjustment != nums2[p]:
                    return False
                return loop_check(p + 1)
            return loop_check(0)

        def build_subset(skip_start: int, skip_end: int) -> List[int]:
            temp_list = []
            pos = 0
            while pos < skip_start:
                temp_list.append(nums1[pos])
                pos += 1
            pos = skip_start + 1
            while pos < skip_end:
                temp_list.append(nums1[pos])
                pos += 1
            pos = skip_end + 1
            while pos < m:
                temp_list.append(nums1[pos])
                pos += 1
            return temp_list

        outer_index = 0
        while outer_index < m - 1:
            inner_index = outer_index + 1
            while inner_index < m:
                candidate_subset = build_subset(outer_index, inner_index)
                if not candidate_subset or len(candidate_subset) < n:
                    inner_index += 1
                    continue
                proposed_x = nums2[0] - candidate_subset[0]

                if check_adjusted(candidate_subset, proposed_x):
                    return proposed_x

                inner_index += 1
            outer_index += 1

        return None