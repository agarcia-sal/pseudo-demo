class Solution:
    def earliestSecondToMarkIndices(self, nums, changeIndices):
        length_nums = len(nums)
        length_changes = len(changeIndices)

        def can_mark_by_second(k):
            last_seen = [-1] * length_nums
            for index in range(k):
                position = changeIndices[index] - 1
                last_seen[position] = index

            required_total = sum(nums)
            decrement_pool = 0
            marked_set = set()
            step = 0
            while step < k:
                current_pos = changeIndices[step] - 1
                if current_pos not in marked_set:
                    if last_seen[current_pos] == step:
                        if nums[current_pos] <= decrement_pool:
                            decrement_pool -= nums[current_pos]
                            marked_set.add(current_pos)
                        else:
                            return False
                    else:
                        decrement_pool += 1
                else:
                    decrement_pool += 1
                step += 1
            return len(marked_set) == length_nums

        low, high = 0, length_changes + 1
        while low < high:
            middle = low + (high - low) // 2
            if can_mark_by_second(middle):
                high = middle
            else:
                low += 1

        return low if low <= length_changes else -1