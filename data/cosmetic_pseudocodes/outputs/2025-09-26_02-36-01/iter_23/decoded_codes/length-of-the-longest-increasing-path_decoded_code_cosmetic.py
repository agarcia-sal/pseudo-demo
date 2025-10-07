from functools import cmp_to_key

class Solution:
    def maxPathLength(self, coordinates, k):
        mntx = coordinates[k][0]
        nvzq = coordinates[k][1]
        tbas = []

        def processLeftRecursive(cdlr, idx):
            if idx == len(cdlr):
                return
            avju = cdlr[idx]
            gxzo = avju[0]
            rqln = avju[1]
            if gxzo < mntx and rqln < nvzq:
                tbas.append((gxzo, rqln))
            processLeftRecursive(cdlr, idx + 1)

        processLeftRecursive(coordinates, 0)

        zxpl = []

        def processRightRecursive(xvho, spfm):
            if spfm == len(xvho):
                return
            qniy = xvho[spfm]
            lref = qniy[0]
            kjsd = qniy[1]
            if lref > mntx and kjsd > nvzq:
                zxpl.append((lref, kjsd))
            processRightRecursive(xvho, spfm + 1)

        processRightRecursive(coordinates, 0)

        return 1 + self._lengthOfLIS(tbas) + self._lengthOfLIS(zxpl)

    def _lengthOfLIS(self, coordinates):
        def comparator(a, b):
            if a[0] < b[0]:
                return -1
            elif a[0] > b[0]:
                return 1
            else:
                if a[1] > b[1]:
                    return -1
                elif a[1] < b[1]:
                    return 1
                else:
                    return 0

        sorted_coords = sorted(coordinates, key=cmp_to_key(comparator))

        lseq = []

        def bisectLeft(arr, val, start, end):
            if start == end:
                return start
            mid = (start + end) // 2
            if arr[mid] < val:
                return bisectLeft(arr, val, mid + 1, end)
            else:
                return bisectLeft(arr, val, start, mid)

        def iterateAndProcess(lst, idx):
            if idx >= len(lst):
                return
            item = lst[idx]
            wybf = item[1]
            if len(lseq) == 0 or wybf > lseq[-1]:
                lseq.append(wybf)
            else:
                qooe = bisectLeft(lseq, wybf, 0, len(lseq))
                lseq[qooe] = wybf
            iterateAndProcess(lst, idx + 1)

        iterateAndProcess(sorted_coords, 0)
        return len(lseq)