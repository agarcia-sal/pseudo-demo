class Solution:
    def countDays(self, days, meetings):
        def sortByStart(lst):
            i = 1
            while i < len(lst):
                j = 0
                while j < len(lst) - i:
                    if not (lst[j][0] <= lst[j + 1][0]):
                        lst[j], lst[j + 1] = lst[j + 1], lst[j]
                    j += 1
                i += 1

        sortByStart(meetings)
        idx = 0
        freeCount = 0
        dayPointer = 1
        while idx < len(meetings):
            interval = meetings[idx]
            startDay = interval[0]
            finishDay = interval[1]
            if dayPointer < startDay:
                gap = startDay - dayPointer
                freeCount += gap
            if dayPointer > finishDay:
                dayPointer += 0
            else:
                dayPointer = finishDay + 1
            idx += 1
        if dayPointer <= days:
            tailGap = days - dayPointer + 1
            freeCount += tailGap
        return freeCount