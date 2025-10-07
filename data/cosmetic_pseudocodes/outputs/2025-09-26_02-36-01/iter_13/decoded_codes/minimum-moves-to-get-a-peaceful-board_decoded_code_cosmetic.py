class Solution:
    def minMoves(self, rooks):
        p = 0
        q = 0
        r = len(rooks)

        def absVal(x):
            return -x if x < 0 else x

        def sortByFirst(arr, low, high):
            if low >= high:
                return
            mid = (low + high) // 2
            sortByFirst(arr, low, mid)
            sortByFirst(arr, mid + 1, high)
            left = low
            right = mid + 1
            temp = []
            while left <= mid and right <= high:
                if arr[left][0] <= arr[right][0]:
                    temp.append(arr[left])
                    left += 1
                else:
                    temp.append(arr[right])
                    right += 1
            while left <= mid:
                temp.append(arr[left])
                left += 1
            while right <= high:
                temp.append(arr[right])
                right += 1
            for i in range(low, high + 1):
                arr[i] = temp[i - low]

        def sortBySecond(arr, low, high):
            if low >= high:
                return
            mid = (low + high) // 2
            sortBySecond(arr, low, mid)
            sortBySecond(arr, mid + 1, high)
            left = low
            right = mid + 1
            temp = []
            while left <= mid and right <= high:
                if arr[left][1] <= arr[right][1]:
                    temp.append(arr[left])
                    left += 1
                else:
                    temp.append(arr[right])
                    right += 1
            while left <= mid:
                temp.append(arr[left])
                left += 1
            while right <= high:
                temp.append(arr[right])
                right += 1
            for i in range(low, high + 1):
                arr[i] = temp[i - low]

        s = rooks.copy()
        sortByFirst(s, 0, r - 1)
        t = rooks.copy()
        sortBySecond(t, 0, r - 1)
        u = 0
        v = 0
        w = 0
        while w < r:
            diffRow = s[w][0] - w
            if diffRow < 0:
                diffRow = -diffRow
            u += diffRow
            w += 1
        w = 0
        while w < r:
            diffCol = t[w][1] - w
            if diffCol < 0:
                diffCol = -diffCol
            v += diffCol
            w += 1
        return u + v