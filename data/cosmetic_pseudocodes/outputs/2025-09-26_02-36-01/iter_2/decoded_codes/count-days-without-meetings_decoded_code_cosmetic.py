from typing import List

class Solution:
    def countDays(self, total_days: int, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])

        pointer = 1
        free_days = 0
        index = 0
        length = len(intervals)

        while index < length:
            interval = intervals[index]
            start_day, finish_day = interval

            if pointer < start_day:
                gap = start_day - pointer
                free_days += gap

            next_pointer = finish_day + 1
            if next_pointer > pointer:
                pointer = next_pointer

            index += 1

        if pointer <= total_days:
            remaining = total_days - pointer + 1
            free_days += remaining

        return free_days