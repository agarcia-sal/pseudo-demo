from typing import List, Tuple

class Solution:
    def maxPathLength(self, coordinates: List[Tuple[int, int]], k: int) -> int:
        alpha = coordinates[k][0]
        bravo = coordinates[k][1]
        charlie = []
        echo = []
        delta = 0

        length = len(coordinates)
        while delta < length:
            golf = coordinates[delta][0]
            hotel = coordinates[delta][1]
            if not (golf >= alpha or hotel >= bravo):
                charlie.append((golf, hotel))
            delta += 1

        delta = 0
        while delta < length:
            golf = coordinates[delta][0]
            hotel = coordinates[delta][1]
            if golf > alpha and hotel > bravo:
                echo.append((golf, hotel))
            delta += 1

        return 1 + self._lengthOfLIS(charlie) + self._lengthOfLIS(echo)

    def _lengthOfLIS(self, coordinates: List[Tuple[int, int]]) -> int:
        def bisectLeft(array: List[int], target: int) -> int:
            left, right = 0, len(array)
            while left < right:
                mid = left + (right - left) // 2
                if array[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left

        # Sort by x ascending, then by y descending
        tempCoordinates = sorted(coordinates, key=lambda x: (x[0], -x[1]))
        tail = []

        for _, currentY in tempCoordinates:
            if not tail or tail[-1] < currentY:
                tail.append(currentY)
            else:
                pos = bisectLeft(tail, currentY)
                tail[pos] = currentY

        return len(tail)