from typing import List

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        available_days = 0
        current_day = 1
        meetings.sort(key=lambda meeting: meeting[0])

        for meeting in meetings:
            start, end = meeting
            if current_day < start:
                available_days += start - current_day
            if end + 1 > current_day:
                current_day = end + 1

        if current_day <= days:
            available_days += days - current_day + 1

        return available_days