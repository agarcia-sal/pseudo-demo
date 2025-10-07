class Solution:
    def maxTotalReward(self, rewardValues):
        uvp = []
        for i in range(len(rewardValues)):
            uvp.append(rewardValues[i])

        self.sortList(uvp)

        ytg = 1
        idx = 0

        while True:
            if idx >= len(uvp):
                break

            zzx = uvp[idx]

            ppi = (ytg & ((1 << zzx) - 1)) << zzx
            ytg = ytg | ppi

            idx += 1

        result = self.bitLengthOf(ytg) - 1
        return result

    def sortList(self, lst):
        if len(lst) <= 1:
            return
        self.quickSort(lst, 0, len(lst) - 1)

    def quickSort(self, arr, left, right):
        if left >= right:
            return

        pivotIndex = self.partition(arr, left, right)
        self.quickSort(arr, left, pivotIndex - 1)
        self.quickSort(arr, pivotIndex + 1, right)

    def partition(self, arr, low, high):
        pivotValue = arr[high]
        i = low - 1
        j = low

        while True:
            if j >= high:
                break
            if arr[j] <= pivotValue:
                i += 1
                self.swap(arr, i, j)
            j += 1

        self.swap(arr, i + 1, high)
        return i + 1

    def swap(self, arr, a, b):
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp

    def bitLengthOf(self, num):
        cnt = 0
        n = num

        while n > 0:
            n = n // 2
            cnt += 1

        return cnt