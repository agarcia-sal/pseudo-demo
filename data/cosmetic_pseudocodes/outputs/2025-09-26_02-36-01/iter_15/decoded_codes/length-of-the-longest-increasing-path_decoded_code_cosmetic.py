from typing import List, Tuple

class Solution:
    def maxPathLength(self, coordinates: List[Tuple[int, int]], k: int) -> int:
        eta, zeta = coordinates[k]
        omega = []
        gamma = 0
        while gamma < len(coordinates):
            alpha, beta = coordinates[gamma]
            if not (alpha >= eta or beta >= zeta):
                omega.append((alpha, beta))
            gamma += 1
        psi = []
        delta = 0
        while delta < len(coordinates):
            mu, nu = coordinates[delta]
            if mu > eta and nu > zeta:
                psi.append((mu, nu))
            delta += 1
        return 1 + self._lengthOfLIS(omega) + self._lengthOfLIS(psi)

    def _lengthOfLIS(self, coordinates: List[Tuple[int, int]]) -> int:
        def custom_bisect_left(array: List[int], target: int) -> int:
            left_bound, right_bound = 0, len(array)
            while left_bound < right_bound:
                mid = left_bound + (right_bound - left_bound) // 2
                if array[mid] < target:
                    left_bound = mid + 1
                else:
                    right_bound = mid
            return left_bound

        sortedList = coordinates[:]

        # Bubble sort with custom condition:
        # (c1[0] > c2[0]) OR (c1[0] == c2[0] AND c1[1] < c2[1])
        # Sort ascending by first coordinate, if tie descending by second coordinate
        swapped = True
        while swapped:
            swapped = False
            idx1 = 0
            while idx1 < len(sortedList) - 1:
                c1, c2 = sortedList[idx1], sortedList[idx1+1]
                if (c1[0] > c2[0]) or (c1[0] == c2[0] and c1[1] < c2[1]):
                    sortedList[idx1], sortedList[idx1+1] = c2, c1
                    swapped = True
                idx1 += 1

        accumulator = []
        walker = 0
        while walker < len(sortedList):
            coord_y = sortedList[walker][1]
            if not accumulator or coord_y > accumulator[-1]:
                accumulator.append(coord_y)
            else:
                pos = custom_bisect_left(accumulator, coord_y)
                accumulator[pos] = coord_y
            walker += 1
        return len(accumulator)