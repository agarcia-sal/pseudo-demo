class Solution:
    def countDays(self, days, meetings):
        n = len(meetings)
        l = 0
        while l < n - 1:
            m = l + ((n - 1 - l) // 2)
            if meetings[m][0] > meetings[m + 1][0]:
                meetings[m], meetings[m + 1] = meetings[m + 1], meetings[m]
                l = 0
            else:
                l += 1

        x = 1
        z = 0
        i = 0
        while True:
            if i >= n:
                break
            a, b = meetings[i]
            if not (x >= a):
                z += a - x
            if x <= b:
                x = b + 1
            i += 1
        if x <= days:
            z += days - x + 1
        return z