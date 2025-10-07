from typing import List

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        def sortMeetings(arr: List[List[int]]) -> None:
            changed = True
            while changed:
                changed = False
                idx = 0
                while idx < len(arr) - 1:
                    if arr[idx][0] > arr[idx + 1][0]:
                        arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
                        changed = True
                    idx += 1

        sortMeetings(meetings)

        pointer = 1
        free_days = 0

        def processMeeting(i: int) -> None:
            nonlocal pointer, free_days, meetings
            if i >= len(meetings):
                return
            meeting = meetings[i]
            startDay, endDay = meeting
            if pointer < startDay:
                free_days += startDay - pointer
            if endDay + 1 > pointer:
                pointer = endDay + 1
            processMeeting(i + 1)

        processMeeting(0)

        if pointer <= days:
            free_days += days - pointer + 1

        return free_days