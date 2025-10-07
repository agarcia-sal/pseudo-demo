from typing import List, Tuple

class Solution:
    def countDays(self, days: int, meetings: List[Tuple[int, int]]) -> int:
        def sortMeetings(index: int, length: int, arr: List[Tuple[int, int]]) -> None:
            if index >= length - 1:
                return
            minIdx = index
            j = index + 1
            while j < length:
                if arr[j][0] < arr[minIdx][0]:
                    minIdx = j
                j += 1
            if minIdx != index:
                arr[index], arr[minIdx] = arr[minIdx], arr[index]
            sortMeetings(index + 1, length, arr)

        sortMeetings(0, len(meetings), meetings)

        dayCursor = 1
        freeDaysCount = 0

        def processMeetings(pos: int, total: int, meets: List[Tuple[int, int]], curr: int, freeCount: int) -> int:
            if pos == total:
                return freeCount
            meetStart, meetEnd = meets[pos]

            if curr < meetStart:
                freeCount += meetStart - curr

            nextDay = curr if curr > meetEnd else meetEnd + 1
            return processMeetings(pos + 1, total, meets, nextDay, freeCount)

        freeDaysCount = processMeetings(0, len(meetings), meetings, dayCursor, freeDaysCount)

        # After processing meetings, determine if there remain any free days until the total days
        # dayCursor in pseudocode doesn't change in main function after initialization, so using
        # the equivalent logic: The final current day after meetings is the nextDay from last meeting
        # But here dayCursor remains 1; we need to track current day after meetings:
        # So instead of dayCursor, store final curr day during processing by processMeetings return.

        # To capture the final dayCursor correctly, we can modify processMeetings to return a tuple: (freeCount, finalCurr)
        # but this modifies the original structure. Alternatively, recompute the occupied days and find total free days from that.

        # According to pseudocode:
        # After processMeetings, if dayCursor <= days:
        #     gap = days - dayCursor + 1
        #     freeDaysCount += gap
        # if dayCursor > days then available = freeDaysCount else available = freeDaysCount
        # This suggests available = freeDaysCount always

        # However, in the pseudocode, dayCursor seems never updated after initialization
        # The pseudocode likely contains an inconsistency in usage of dayCursor at the end
        # We will interpret dayCursor as the current day after processing meetings (the nextDay in last call)

        # We can track dayCursor by modifying processMeetings to return freeCount and final curr day
        def processMeetings_v2(pos: int, total: int, meets: List[Tuple[int, int]], curr: int, freeCount: int) -> Tuple[int, int]:
            if pos == total:
                return freeCount, curr
            meetStart, meetEnd = meets[pos]

            if curr < meetStart:
                freeCount += meetStart - curr

            nextDay = curr if curr > meetEnd else meetEnd + 1
            return processMeetings_v2(pos + 1, total, meets, nextDay, freeCount)

        freeDaysCount, dayCursor = processMeetings_v2(0, len(meetings), meetings, dayCursor, freeDaysCount)

        if dayCursor <= days:
            gap = days - dayCursor + 1
            freeDaysCount += gap

        available = freeDaysCount

        return available