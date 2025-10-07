class Solution:
    def earliestSecondToMarkIndices(self, changeIndices: list[int], nums: list[int]) -> int:
        length_nums = len(nums)
        length_changes = len(changeIndices)

        def can_mark_by_second(limit: int) -> bool:
            # Initialize list of size length_nums with value -1
            last_occurrence_array = [-1] * length_nums

            # Fill last_occurrence_array with the last occurrence index of each position up to 'limit'
            for index in range(limit):
                original_pos = changeIndices[index] - 1
                last_occurrence_array[original_pos] = index

            needed_decrement_total = sum(nums)
            spare_decrements = 0
            marked_set = set()
            can_mark_result = True

            # Process each second s up to 'limit'
            s = 0
            while s < limit and can_mark_result:
                idx_pos = changeIndices[s] - 1
                if idx_pos not in marked_set:
                    if last_occurrence_array[idx_pos] == s:
                        if nums[idx_pos] <= spare_decrements:
                            spare_decrements -= nums[idx_pos]
                            marked_set.add(idx_pos)
                        else:
                            can_mark_result = False
                            break
                    else:
                        spare_decrements += 1
                else:
                    spare_decrements += 1
                s += 1

            return can_mark_result and (len(marked_set) == length_nums)

        low_bound = 0
        high_bound = length_changes + 1

        def binary_search(low: int, high: int) -> int:
            while low < high:
                mid_point = (low + high) // 2
                if can_mark_by_second(mid_point):
                    high = mid_point
                else:
                    low = mid_point + 1
            return low

        answer = binary_search(low_bound, high_bound)

        if answer <= length_changes:
            return answer
        else:
            return -1