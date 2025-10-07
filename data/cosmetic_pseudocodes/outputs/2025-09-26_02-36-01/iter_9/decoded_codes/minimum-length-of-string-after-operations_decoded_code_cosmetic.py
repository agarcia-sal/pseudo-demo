class Solution:
    def minimumLength(self, t):
        def tallyElements(u):
            w = {}
            def incrementDict(k):
                if k in w:
                    w[k] += 1
                else:
                    w[k] = 1
            i = 0
            while True:
                if i >= len(u):
                    break
                incrementDict(u[i])
                i += 1
            return w

        z = tallyElements(t)

        def isOdd(nv):
            return (nv % 2) == 1

        def isNonZeroEven(nv):
            return (nv % 2) == 0 and nv != 0

        accumOdd = 0
        accumEven = 0

        vals = []
        def collectValues(dictValues):
            for val in dictValues:
                vals.append(val)

        collectValues(z.values())

        def processAtIndex(idx):
            nonlocal accumOdd, accumEven
            if idx >= len(vals):
                return
            currentValue = vals[idx]
            if isOdd(currentValue):
                accumOdd += 1
            else:
                if isNonZeroEven(currentValue):
                    accumEven += 2
            processAtIndex(idx + 1)

        processAtIndex(0)

        wResult = accumOdd + accumEven

        return wResult