from typing import List, Optional

class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> Optional[int]:
        nums1.sort()
        nums2.sort()

        len_nums1 = len(nums1)
        len_nums2 = len(nums2)

        outer_idx = 0
        while outer_idx < len_nums1 - 1:
            inner_idx = outer_idx + 1
            while inner_idx < len_nums1:
                filtered_nums1 = []

                # Append elements before outer_idx
                cur_pos = 0
                while cur_pos < outer_idx:
                    filtered_nums1.append(nums1[cur_pos])
                    cur_pos += 1

                # Append elements between outer_idx and inner_idx (excluding these two indices)
                cur_pos = outer_idx + 1
                while cur_pos < inner_idx:
                    filtered_nums1.append(nums1[cur_pos])
                    cur_pos += 1

                # Append elements after inner_idx
                cur_pos = inner_idx + 1
                while cur_pos < len_nums1:
                    filtered_nums1.append(nums1[cur_pos])
                    cur_pos += 1

                # If filtered_nums1 is empty or shorter than nums2, no valid shift possible
                if not filtered_nums1 or len(filtered_nums1) < len_nums2:
                    inner_idx += 1
                    continue

                first_diff = nums2[0] - filtered_nums1[0]
                valid_shift = True

                idx_check = 0
                while idx_check < len_nums2:
                    check_val = filtered_nums1[idx_check] + first_diff
                    if check_val != nums2[idx_check]:
                        valid_shift = False
                        break
                    idx_check += 1

                if valid_shift:
                    return first_diff

                inner_idx += 1
            outer_idx += 1

        return None