class Solution:
    def countDays(self, days: int, meetings: list[list[int]]) -> int:
        meetings.sort(key=lambda x: x[0])
        current_day = 1
        available_days = 0
        for meeting in meetings:
            start, end = meeting
            if current_day < start:
                available_days += start - current_day
            current_day = max(current_day, end) + 1
        if current_day <= days:
            available_days += days - current_day + 1
        return available_days