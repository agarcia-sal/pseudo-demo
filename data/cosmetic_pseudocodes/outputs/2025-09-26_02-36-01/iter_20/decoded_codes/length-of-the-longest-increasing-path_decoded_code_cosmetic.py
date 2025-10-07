from typing import List, Tuple

class Solution:
    def maxPathLength(self, coordinates: List[Tuple[int, int]], k: int) -> int:
        alpha = coordinates[k][0]
        beta = coordinates[k][1]

        setA = []
        idxA = 0
        while idxA < len(coordinates):
            vx, vy = coordinates[idxA]
            if not (vx >= alpha) and not (vy >= beta):
                setA.append((vx, vy))
            idxA += 1

        setB = []
        idxB = 0
        while True:
            if idxB >= len(coordinates):
                break
            px, py = coordinates[idxB]
            if px > alpha and py > beta:
                setB.append((px, py))
            idxB += 1

        return 1 + self._lengthOfLIS(setA) + self._lengthOfLIS(setB)

    def _lengthOfLIS(self, coordinates: List[Tuple[int, int]]) -> int:
        def compare(a: Tuple[int, int], b: Tuple[int, int]) -> int:
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

        def merge_sort(arr: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
            if len(arr) <= 1:
                return arr
            mid_idx = len(arr) // 2
            left_part = merge_sort(arr[:mid_idx])
            right_part = merge_sort(arr[mid_idx:])
            return merge(left_part, right_part)

        def merge(left_arr: List[Tuple[int, int]], right_arr: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
            merged = []
            l_i = 0
            r_i = 0
            while l_i < len(left_arr) and r_i < len(right_arr):
                if compare(left_arr[l_i], right_arr[r_i]) <= 0:
                    merged.append(left_arr[l_i])
                    l_i += 1
                else:
                    merged.append(right_arr[r_i])
                    r_i += 1
            while l_i < len(left_arr):
                merged.append(left_arr[l_i])
                l_i += 1
            while r_i < len(right_arr):
                merged.append(right_arr[r_i])
                r_i += 1
            return merged

        def binary_search_left(arr: List[int], target: int) -> int:
            left, right = 0, len(arr)
            while left < right:
                mid = left + (right - left) // 2
                if arr[mid] >= target:
                    right = mid
                else:
                    left = mid + 1
            return left

        sorted_coords = merge_sort(coordinates)
        seq = []
        i = 0
        while i < len(sorted_coords):
            elem = sorted_coords[i][1]
            if not seq or elem > seq[-1]:
                seq.append(elem)
            else:
                pos = binary_search_left(seq, elem)
                seq[pos] = elem
            i += 1
        return len(seq)