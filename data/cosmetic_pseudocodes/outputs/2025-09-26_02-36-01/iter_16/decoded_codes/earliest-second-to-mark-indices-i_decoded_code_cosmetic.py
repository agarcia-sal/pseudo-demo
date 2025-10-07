class Solution:
    def earliestSecondToMarkIndices(self, nums, changeIndices):
        count_elements = len(nums)
        count_changes = len(changeIndices)

        def can_mark_by_second(k):
            positions = [-1] * count_elements
            step = 0
            while step < k:
                pos_index = changeIndices[step] - 1
                positions[pos_index] = step
                step += 1

            needed_dec = sum(nums)
            available_dec = 0
            indices_marked = set()

            iter_counter = 0
            while True:
                if iter_counter >= k:
                    break
                current_idx = changeIndices[iter_counter] - 1
                if current_idx not in indices_marked:
                    if positions[current_idx] == iter_counter:
                        if nums[current_idx] <= available_dec:
                            available_dec -= nums[current_idx]
                            indices_marked.add(current_idx)
                        else:
                            return False
                    else:
                        available_dec += 1
                else:
                    available_dec += 1
                iter_counter += 1

            return len(indices_marked) == count_elements

        low = 0
        high = count_changes + 1

        def calculate_midpoint(a, b):
            return (a + b) // 2

        while low < high:
            middle = calculate_midpoint(low, high)
            if can_mark_by_second(middle):
                high = middle
            else:
                low = low + 1

        if low <= count_changes:
            return low
        else:
            return -1