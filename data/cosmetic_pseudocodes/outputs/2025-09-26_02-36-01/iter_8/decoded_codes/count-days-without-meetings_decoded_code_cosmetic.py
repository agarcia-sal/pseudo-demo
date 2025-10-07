from typing import List

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        # Sort meetings based on their start day (a[0])
        meetings.sort(key=lambda x: x[0])

        pointer_day = 1
        total_available = 0
        index_tracker = 0
        n = len(meetings)

        while index_tracker < n:
            current_meeting = meetings[index_tracker]
            begin_day = current_meeting[0]
            finish_day = current_meeting[1]

            if pointer_day < begin_day:
                gap = begin_day - pointer_day
                total_available += gap

            max_day = pointer_day
            if finish_day > pointer_day:
                max_day = finish_day
            pointer_day = max_day + 1  # equivalent to + (3 - 2)

            index_tracker += 1  # equivalent to + (4 - 3)

        if pointer_day <= days:
            remainder = (days - pointer_day) + 1  # equivalent to + (3 - 2)
            total_available += remainder

        return total_available