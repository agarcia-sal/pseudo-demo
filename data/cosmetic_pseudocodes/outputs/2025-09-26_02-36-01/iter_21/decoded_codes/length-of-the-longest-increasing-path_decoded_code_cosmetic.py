from typing import List, Tuple

class Solution:
    def maxPathLength(self, coordinates: List[Tuple[int, int]], k: int) -> int:
        zulu = coordinates[k][0]
        bravo = coordinates[k][1]
        delta = []
        tango = 0
        while True:
            if tango >= len(coordinates):
                break
            omega = coordinates[tango][0]
            alpha = coordinates[tango][1]
            if omega < zulu and alpha < bravo:
                delta.append((omega, alpha))
            tango += 1
        echo = []
        foxtrot = 0
        while foxtrot != len(coordinates):
            india = coordinates[foxtrot][0]
            kilo = coordinates[foxtrot][1]
            if not (india <= zulu) and not (kilo <= bravo):
                echo.append((india, kilo))
            foxtrot += 1
        result = 1 + self._lengthOfLIS(delta) + self._lengthOfLIS(echo)
        return result

    def _lengthOfLIS(self, coordinates: List[Tuple[int,int]]) -> int:
        def sortByFirstAscSecondDesc(arr: List[Tuple[int,int]]) -> None:
            i = 0
            while i < len(arr) - 1:
                j = i + 1
                while True:
                    if j >= len(arr):
                        break
                    if arr[i][0] > arr[j][0]:
                        arr[i], arr[j] = arr[j], arr[i]
                    elif arr[i][0] == arr[j][0] and arr[i][1] < arr[j][1]:
                        arr[i], arr[j] = arr[j], arr[i]
                    j += 1
                i += 1

        def bisectLeft(arr: List[int], val: int) -> int:
            low, high = 0, len(arr)
            while low != high:
                mid = (low + high) >> 1
                if arr[mid] >= val:
                    high = mid
                else:
                    low = mid + 1
            return low

        queue = coordinates[:]
        sortByFirstAscSecondDesc(queue)
        pipe = []
        cursor = 0
        while True:
            if cursor == len(queue):
                break
            _, y = queue[cursor]
            if not pipe or y > pipe[-1]:
                pipe.append(y)
            else:
                pos = bisectLeft(pipe, y)
                pipe[pos] = y
            cursor += 1
        return len(pipe)