class Solution:
    def maxPathLength(self, coordinates, k):
        refX = coordinates[k][0]
        refY = coordinates[k][1]

        accLeft = []

        def collectLeft(idx):
            if idx == len(coordinates):
                return
            currX, currY = coordinates[idx]
            if not (currX >= refX) and not (currY >= refY):
                accLeft.append((currX, currY))
            collectLeft(idx + 1)

        collectLeft(0)

        accRight = []

        def collectRight(pos):
            if pos == len(coordinates):
                return
            valX, valY = coordinates[pos]
            if valX > refX and valY > refY:
                accRight.append((valX, valY))
            collectRight(pos + 1)

        collectRight(0)

        leftLen = self._lengthOfLIS(accLeft)
        rightLen = self._lengthOfLIS(accRight)
        result = 1 + leftLen + rightLen
        return result

    def _lengthOfLIS(self, coordinates):
        def comparePoints(a, b):
            if a[0] < b[0]:
                return True
            elif a[0] == b[0]:
                return a[1] > b[1]
            else:
                return False

        def insertionSort(arr):
            n = len(arr)
            for i in range(1, n):
                key = arr[i]
                j = i - 1
                while j >= 0 and not comparePoints(arr[j], key):
                    arr[j + 1] = arr[j]
                    j -= 1
                arr[j + 1] = key
            return arr

        sortedCoords = insertionSort(coordinates)

        tails = []

        def bisectLeft(listTails, target):
            low, high = 0, len(listTails)
            while low < high:
                mid = (low + high) // 2
                if listTails[mid] < target:
                    low = mid + 1
                else:
                    high = mid
            return low

        def process(idx):
            if idx == len(sortedCoords):
                return
            valY = sortedCoords[idx][1]
            if len(tails) == 0 or valY > tails[-1]:
                tails.append(valY)
            else:
                pos = bisectLeft(tails, valY)
                tails[pos] = valY
            process(idx + 1)

        process(0)

        return len(tails)