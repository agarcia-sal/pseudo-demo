class Solution:
    def countDays(self, days, meetings):
        def ascendingCompare(a, b):
            return 1 if a[0] > b[0] else 0

        idx = 0
        length = len(meetings)
        # Bubble sort to sort meetings by start day
        while idx < length - 1:
            inner = 0
            while inner < length - idx - 1:
                if ascendingCompare(meetings[inner], meetings[inner + 1]) > 0:
                    meetings[inner], meetings[inner + 1] = meetings[inner + 1], meetings[inner]
                inner += 1
            idx += 1

        v = 1
        w = 0
        p = 0

        while p < length:
            q = meetings[p][0]
            r = meetings[p][1]

            if v < q:
                tempDiff = q - v
                w += tempDiff

            if v > r:
                v = v
            else:
                v = r + 1

            p += 1

        if v <= days:
            extra = days - v + 1
            w += extra

        return w