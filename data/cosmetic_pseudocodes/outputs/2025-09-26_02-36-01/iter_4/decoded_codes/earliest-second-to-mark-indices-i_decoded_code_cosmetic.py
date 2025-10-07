class Solution:
    def earliestSecondToMarkIndices(self, nums, changeIndices):
        totalElements = len(nums)
        totalChanges = len(changeIndices)

        def can_mark_by_second(k):
            recent_positions = [-1] * totalElements
            index_counter = 0
            while index_counter < k:
                currentIndex = changeIndices[index_counter] - 1
                recent_positions[currentIndex] = index_counter
                index_counter += 1

            decrements_available = 0
            marked_set = set()

            step = 0
            while step < k:
                pos = changeIndices[step] - 1
                if pos not in marked_set:
                    if recent_positions[pos] == step:
                        if nums[pos] <= decrements_available:
                            decrements_available -= nums[pos]
                            marked_set.add(pos)
                        else:
                            return False
                    else:
                        decrements_available += 1
                else:
                    decrements_available += 1
                step += 1

            return len(marked_set) == totalElements

        low, high = 0, totalChanges + 1
        while low < high:
            middle = (low + high) // 2
            if can_mark_by_second(middle):
                high = middle
            else:
                low += 1

        return low if low <= totalChanges else -1