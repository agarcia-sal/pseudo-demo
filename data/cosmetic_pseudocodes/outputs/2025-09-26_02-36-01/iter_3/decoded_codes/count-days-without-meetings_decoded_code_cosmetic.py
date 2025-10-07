class Solution:
    def countDays(self, days, meetings):
        sortedMeetings = meetings[:]
        index = 0
        while index < len(sortedMeetings) - 1:
            j = 0
            while j < len(sortedMeetings) - index - 1:
                if sortedMeetings[j][0] > sortedMeetings[j + 1][0]:
                    sortedMeetings[j], sortedMeetings[j + 1] = sortedMeetings[j + 1], sortedMeetings[j]
                j += 1
            index += 1

        dayCursor = 1
        freeDayCount = 0
        i = 0
        while i < len(sortedMeetings):
            beginDay, finishDay = sortedMeetings[i]
            if dayCursor < beginDay:
                gap = beginDay - dayCursor
                freeDayCount += gap
            if dayCursor <= finishDay:
                dayCursor = finishDay + 1
            i += 1

        if dayCursor <= days:
            remainder = (days - dayCursor) + 1
            freeDayCount += remainder

        return freeDayCount