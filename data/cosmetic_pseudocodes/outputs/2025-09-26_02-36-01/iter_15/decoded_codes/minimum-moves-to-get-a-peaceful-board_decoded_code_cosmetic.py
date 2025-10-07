class Solution:
    def minMoves(self, rooks):
        q = len(rooks)

        def sortByFirstElement(arr):
            if len(arr) <= 1:
                return arr
            pivot = arr[0]
            leftPartition = []
            rightPartition = []
            for i in range(1, len(arr)):
                if arr[i][0] <= pivot[0]:
                    leftPartition.append(arr[i])
                else:
                    rightPartition.append(arr[i])
            return sortByFirstElement(leftPartition) + [pivot] + sortByFirstElement(rightPartition)

        def sortBySecondElement(arr):
            if len(arr) <= 1:
                return arr
            pivot = arr[0]
            leftSet = []
            rightSet = []
            j = 1
            while j < len(arr):
                if arr[j][1] <= pivot[1]:
                    leftSet.append(arr[j])
                else:
                    rightSet.append(arr[j])
                j += 1
            return sortBySecondElement(leftSet) + [pivot] + sortBySecondElement(rightSet)

        h = sortByFirstElement(rooks)
        k = sortBySecondElement(rooks)

        s = 0
        t = 0
        while t < q:
            m = h[t][0] - t
            if m < 0:
                m = -m
            s += m
            t += 1

        x = 0
        y = 0
        while y < q:
            w = k[y][1] - y
            if w < 0:
                w = -w
            x += w
            y += 1

        return s + x