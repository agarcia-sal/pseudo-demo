class Solution:
    def countDays(self, days, meetings):
        meetings.sort(key=lambda x: x[0])  # Sort meetings by start day
        tracker_day = 1
        free_days = 0
        idx = 0
        total_meetings = len(meetings)

        while idx < total_meetings:
            meeting_interval = meetings[idx]
            start_day, finish_day = meeting_interval

            if tracker_day < start_day:
                gap = start_day - tracker_day
                free_days += gap

            next_day_candidate = tracker_day
            if finish_day > tracker_day:
                next_day_candidate = finish_day
            tracker_day = next_day_candidate + 1

            idx += 1

        if tracker_day <= days:
            remaining_days = days - tracker_day + 1
            free_days += remaining_days

        return free_days