class Solution:
    def maxPotholes(self, road: str, budget: int) -> int:
        segmentsList = self.SplitRoadByPeriod(road)
        self.SortAscendingByLength(segmentsList)

        totalFixed = 0
        idx = 0

        while idx < len(segmentsList):
            currentSegment = segmentsList[idx]
            segmentLength = len(currentSegment)

            if segmentLength == 0:
                idx += 1
                continue

            requiredCost = segmentLength + 1

            if requiredCost <= budget:
                totalFixed += segmentLength
                budget -= requiredCost
            else:
                while segmentLength > 0 and budget > 0:
                    requiredCost = segmentLength + 1
                    if budget >= requiredCost:
                        totalFixed += segmentLength
                        budget -= requiredCost
                        break
                    segmentLength -= 1
            idx += 1

        return totalFixed

    def SplitRoadByPeriod(self, input: str) -> list[str]:
        pieces = []
        startPos = 0
        for i, ch in enumerate(input):
            if ch == '.':
                pieces.append(input[startPos:i])
                startPos = i + 1
        pieces.append(input[startPos:])
        return pieces

    def SortAscendingByLength(self, list_of_strings: list[str]) -> None:
        def Swap(arr: list[str], x: int, y: int) -> None:
            arr[x], arr[y] = arr[y], arr[x]

        def Partition(arr: list[str], low: int, high: int) -> int:
            pivotValue = len(arr[high])
            i = low - 1
            for j in range(low, high):
                if len(arr[j]) <= pivotValue:
                    i += 1
                    Swap(arr, i, j)
            Swap(arr, i + 1, high)
            return i + 1

        def QuickSort(arr: list[str], low: int, high: int) -> None:
            if low < high:
                partitionIdx = Partition(arr, low, high)
                QuickSort(arr, low, partitionIdx - 1)
                QuickSort(arr, partitionIdx + 1, high)

        QuickSort(list_of_strings, 0, len(list_of_strings) - 1)