class Solution:
    def countDays(self, days, meetings):
        def customSort(lst):
            idx_outer = 0
            while idx_outer < len(lst) - 1:
                idx_inner = 0
                while idx_inner < len(lst) - idx_outer - 1:
                    if compareFirstElement(lst[idx_inner], lst[idx_inner + 1]) > 0:
                        swapElements(lst, idx_inner, idx_inner + 1)
                    idx_inner += 1
                idx_outer += 1

        def compareFirstElement(a, b):
            if a[0] < b[0]:
                return -1
            elif a[0] > b[0]:
                return 1
            else:
                return 0

        def swapElements(arr, i, j):
            arr[i], arr[j] = arr[j], arr[i]

        customSort(meetings)

        varA = 1
        varB = 0

        def maxValue(x, y):
            return x if x >= y else y

        def processListRec(idx):
            nonlocal varA, varB
            if idx >= len(meetings):
                return
            varC = meetings[idx][0]
            varD = meetings[idx][1]
            if varA < varC:
                varB += (varC - varA)
            varE = maxValue(varA, varD)
            varA = varE + 1
            processListRec(idx + 1)

        processListRec(0)

        if varA <= days:
            varB += (days - varA + 1)

        return varB