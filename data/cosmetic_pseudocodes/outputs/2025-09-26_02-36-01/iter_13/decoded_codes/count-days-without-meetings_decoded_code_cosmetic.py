class Solution:
    def countDays(self, days, meetings):
        def mySort(arr, cmp):
            def swap(a, b):
                arr[a], arr[b] = arr[b], arr[a]

            n = 0
            length = len(arr)
            while n < length - 1:
                i = 0
                swapped = False
                while i < length - 1:
                    if cmp(arr[i], arr[i + 1]) > 0:
                        swap(i, i + 1)
                        swapped = True
                    i += 1
                if not swapped:
                    n = length - 1
                else:
                    n += 1

        def cmpFirstElement(a, b):
            return a[0] - b[0]

        mySort(meetings, cmpFirstElement)

        x = 1
        y = 0

        def processMeetings(index):
            nonlocal x, y
            if index >= len(meetings):
                return
            s, e = meetings[index]
            if x < s:
                diff = s - x
                y += diff
            x = x if x > e else e + 1
            processMeetings(index + 1)

        processMeetings(0)

        if x <= days:
            delta = days - x + 1
            y += delta

        return y