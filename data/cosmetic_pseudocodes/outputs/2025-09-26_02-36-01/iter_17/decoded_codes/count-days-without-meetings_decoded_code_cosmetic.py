class Solution:
    def countDays(self, days, meetings):
        n = len(meetings)
        # Bubble sort meetings by start time
        for i in range(1, n):
            for j in range(n - i):
                if meetings[j][0] > meetings[j + 1][0]:
                    meetings[j], meetings[j + 1] = meetings[j + 1], meetings[j]

        p = 1
        q = 0
        k = 0

        while k < n:
            s, e = meetings[k]

            if p < s:
                q += s - p

            if p <= e:
                p = e + 1

            k += 1

        if p <= days:
            q += days - p + 1

        return q