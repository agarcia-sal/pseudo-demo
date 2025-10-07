class Solution:
    def maxSelectedElements(self, nums):
        occurrenceMap = {}
        maximumCount = 0
        sorted_list = sorted(nums)
        for current_number in sorted_list:
            prev_value = occurrenceMap.get(current_number, 0)
            next_value = occurrenceMap.get(current_number + 1, 0)

            occurrenceMap[current_number + 1] = prev_value + 1

            if current_number - 1 in occurrenceMap:
                occurrenceMap[current_number] = occurrenceMap[current_number - 1] + 1
            else:
                occurrenceMap[current_number] = 1

            max_for_current = occurrenceMap[current_number]
            max_for_next = occurrenceMap[current_number + 1]

            local_max = max(max_for_current, max_for_next)

            if local_max > maximumCount:
                maximumCount = local_max

        return maximumCount