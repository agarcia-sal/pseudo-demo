from typing import List, Tuple

class Solution:
    def countDays(self, events: int, schedule: List[Tuple[int, int]]) -> int:
        def compareFirst(a: Tuple[int, int], b: Tuple[int, int]) -> int:
            if a[0] < b[0]:
                return -1
            elif a[0] > b[0]:
                return 1
            else:
                return 0

        def quicksort(lst: List[Tuple[int, int]], left: int, right: int) -> None:
            if left >= right:
                return
            pivotIndex = left
            i, j = left, right
            while i < j:
                while i < right and compareFirst(lst[i], lst[pivotIndex]) <= 0:
                    i += 1
                while j > left and compareFirst(lst[j], lst[pivotIndex]) > 0:
                    j -= 1
                if i < j:
                    lst[i], lst[j] = lst[j], lst[i]
            lst[pivotIndex], lst[j] = lst[j], lst[pivotIndex]
            quicksort(lst, left, j - 1)
            quicksort(lst, j + 1, right)

        quicksort(schedule, 0, len(schedule) - 1)

        dayCounter = 1
        freeDays = 0

        def maxVal(x: int, y: int) -> int:
            return x if x > y else y

        idx = 0
        while idx < len(schedule):
            meetingStart = schedule[idx][0]
            meetingEnd = schedule[idx][1]
            if dayCounter < meetingStart:
                gap = meetingStart - dayCounter
                freeDays += gap
            dayCounter = maxVal(dayCounter, meetingEnd) + 1
            idx += 1

        if dayCounter <= events and not (dayCounter > events):
            remaining = events - dayCounter + 1
            freeDays += remaining

        return freeDays