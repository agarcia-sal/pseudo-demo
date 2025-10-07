class Solution:
    def countDays(self, days, meetings):
        def tsort(mlist):
            # Bubble sort based on the first element of each meeting tuple/list
            def cmp(a, b):
                return (a[0] > b[0]) - (a[0] < b[0])

            sortedList = mlist[:]
            n = len(sortedList)
            i = 0
            while i < n - 1:
                swapped = False
                j = 0
                while j < n - i - 1:
                    if cmp(sortedList[j], sortedList[j + 1]) > 0:
                        sortedList[j], sortedList[j + 1] = sortedList[j + 1], sortedList[j]
                        swapped = True
                    j += 1
                if not swapped:
                    break
                i += 1
            return sortedList

        def maximum(x, y):
            return x if x > y else y

        def minimum(x, y):
            return x if x < y else y

        fDays = 1  # current day after finishing scheduled meetings
        freeSlots = 0

        sortedMeetings = tsort(meetings)

        idx = 0
        totalMeetings = len(sortedMeetings)
        while idx < totalMeetings:
            m = sortedMeetings[idx]
            startDay, finishDay = m[0], m[1]

            if fDays < startDay:
                freeSlots += (startDay - fDays)

            fDays = maximum(fDays, finishDay + 1)
            idx += 1

        if fDays <= days:
            freeSlots += (days - fDays + 1)

        return freeSlots