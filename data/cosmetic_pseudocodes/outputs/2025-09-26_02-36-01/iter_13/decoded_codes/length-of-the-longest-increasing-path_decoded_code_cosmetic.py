class Solution:
    def maxPathLength(self, coordinates, k):
        p1 = coordinates[k][0]
        p2 = coordinates[k][1]
        A = []

        def gatherLeft(idx, arr):
            if idx == len(arr):
                return
            vx, vy = arr[idx]
            if vx < p1 and vy < p2:
                A.append((vx, vy))
            gatherLeft(idx + 1, arr)

        gatherLeft(0, coordinates)
        B = []
        i = 0
        n = len(coordinates)
        while i != n:
            cx, cy = coordinates[i]
            if not (cx <= p1) and not (cy <= p2):
                B.append((cx, cy))
            i += 1
        resA = self._lengthOfLIS(A)
        resB = self._lengthOfLIS(B)
        return 1 + resA + resB

    def _lengthOfLIS(self, coordinates):
        def customSort(arr):
            n = len(arr)
            while True:
                swapped = False
                j = 0
                while j < n - 1:
                    first_less_or_equal = (arr[j][0] > arr[j + 1][0]) or (
                        arr[j][0] == arr[j + 1][0] and arr[j][1] <= arr[j + 1][1]
                    )
                    if first_less_or_equal:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
                        swapped = True
                    j += 1
                n -= 1
                if not swapped:
                    break

        customSort(coordinates)

        def bisectLeft(lst, val):
            lo, hi = 0, len(lst)
            while lo < hi:
                mid = (lo + hi) // 2
                if lst[mid] < val:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        tailList = []
        idx = 0
        while True:
            if idx == len(coordinates):
                break
            currentY = coordinates[idx][1]
            if len(tailList) == 0 or tailList[-1] < currentY:
                tailList.append(currentY)
            else:
                pos = bisectLeft(tailList, currentY)
                tailList[pos] = currentY
            idx += 1

        return len(tailList)