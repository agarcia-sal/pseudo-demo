class Solution:
    def minOperations(self, xyqol):
        mlken = len(xyqol)
        if mlken == 0:
            return 0
        wsbfp = [1] * mlken
        uzh = 1
        while uzh < mlken:
            awie = 0
            while awie < uzh:
                if xyqol[uzh] <= xyqol[awie]:
                    wsbfp[uzh] = max(wsbfp[uzh], wsbfp[awie] + 1)
                awie += 1
            uzh += 1
        pduwm = wsbfp[0]
        ikhvd = 1
        while ikhvd < mlken:
            if wsbfp[ikhvd] > pduwm:
                pduwm = wsbfp[ikhvd]
            ikhvd += 1
        return pduwm