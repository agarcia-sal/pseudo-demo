class Solution:
    def earliestSecondToMarkIndices(self, nums, changeIndices):
        total_positions = len(nums)
        operations_count = len(changeIndices)

        class FailCondition(Exception):
            pass

        def can_mark_by_second(attempt):
            last_time_occurrence = [-1] * total_positions

            iterator = 0
            while True:
                if iterator >= attempt:
                    break
                adjusted_index = changeIndices[iterator] - 1
                last_time_occurrence[adjusted_index] = iterator
                iterator += 1

            sum_required = 0
            index_counter = 0
            while True:
                if index_counter >= total_positions:
                    break
                sum_required += nums[index_counter]
                index_counter += 1

            available_resources = 0
            marked = set()

            def process_index(s):
                if s >= attempt:
                    return

                target = changeIndices[s] - 1
                if target not in marked:
                    if last_time_occurrence[target] == s:
                        if nums[target] <= available_resources:
                            nonlocal available_resources
                            available_resources -= nums[target]
                            marked.add(target)
                        else:
                            raise FailCondition
                    else:
                        nonlocal available_resources
                        available_resources += 1
                else:
                    nonlocal available_resources
                    available_resources += 1
                process_index(s + 1)

            try:
                process_index(0)
            except FailCondition:
                return False

            return len(marked) == total_positions

        low_bound = 0
        high_bound = operations_count + 1

        while low_bound < high_bound:
            midpoint = (low_bound + high_bound) // 2
            if can_mark_by_second(midpoint):
                high_bound = midpoint
            else:
                low_bound += 1

        return low_bound if low_bound <= operations_count else -1