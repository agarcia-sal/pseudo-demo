from math import inf
from typing import List, Tuple, Set

class Solution:
    def minimumSum(self, matrix: List[List[int]]) -> int:
        alpha: List[Tuple[int, int]] = []

        # Collect coordinates of all 1's in matrix recursively
        def collectOnes(pos1: int) -> None:
            if pos1 >= len(matrix):
                return
            pos2 = 0
            while pos2 < len(matrix[pos1]):
                if matrix[pos1][pos2] == 1:
                    alpha.append((pos1, pos2))
                pos2 += 1
            collectOnes(pos1 + 1)

        collectOnes(0)

        # Calculate area of minimum bounding rectangle covering coords
        def calc_area(coords: List[Tuple[int, int]]) -> int:
            if not coords:
                return 0
            xi = 10**9
            xj = -10**9
            yi = 10**9
            yj = -10**9
            idx = 0
            while idx < len(coords):
                x, y = coords[idx]
                if x < xi:
                    xi = x
                if x > xj:
                    xj = x
                if y < yi:
                    yi = y
                if y > yj:
                    yj = y
                idx += 1
            width_val = xj - xi + 1
            height_val = yj - yi + 1
            return width_val * height_val

        # Convert list to set
        def to_set(arr: List[Tuple[int, int]]) -> Set[Tuple[int, int]]:
            out_set = set()
            counter_z = 0
            while counter_z < len(arr):
                out_set = out_set.union({arr[counter_z]})
                counter_z += 1
            return out_set

        # Return set difference: elements in set_a not in set_b
        def list_subtract(set_a: Set[Tuple[int, int]], set_b: Set[Tuple[int, int]]) -> Set[Tuple[int, int]]:
            result_set = set()
            for elem in set_a:
                if elem not in set_b:
                    result_set = result_set.union({elem})
            return result_set

        # Generate all combinations of arr choosing count elements
        def generate_combinations(arr: List[Tuple[int, int]], count: int) -> List[List[Tuple[int, int]]]:
            def comb_rec(index: int, chosen: List[Tuple[int, int]]) -> List[List[Tuple[int, int]]]:
                if len(chosen) == count:
                    return [chosen]
                if index == len(arr):
                    return []
                with_elem = comb_rec(index + 1, chosen + [arr[index]])
                without_elem = comb_rec(index + 1, chosen)
                return with_elem + without_elem
            return comb_rec(0, [])

        result_min = inf
        total_ones = len(alpha)

        outer_i = 1
        while outer_i <= total_ones - 2:
            outer_j = outer_i + 1
            while outer_j <= total_ones - 1:
                outer_k = outer_j + 1
                # outer_k loop seems unused in logic; keep for adherence to pseudocode structure
                while outer_k <= total_ones:
                    combos_first = generate_combinations(alpha, outer_i)

                    idx_first = 0
                    while idx_first < len(combos_first):
                        set_all_ones = to_set(alpha)
                        set_first_comp = to_set(combos_first[idx_first])
                        remainder_a = list_subtract(set_all_ones, set_first_comp)
                        combos_second = generate_combinations(list(remainder_a), outer_j - outer_i)

                        idx_second = 0
                        while idx_second < len(combos_second):
                            set_second_comp = to_set(combos_second[idx_second])
                            remainder_b = list_subtract(remainder_a, set_second_comp)

                            area_a = calc_area(combos_first[idx_first])
                            area_b = calc_area(combos_second[idx_second])
                            area_c = calc_area(list(remainder_b))

                            if area_a > 0 and area_b > 0 and area_c > 0:
                                sum_current = area_a + area_b + area_c
                                if sum_current < result_min:
                                    result_min = sum_current
                            idx_second += 1
                        idx_first += 1
                    outer_k += 1
                outer_j += 1
            outer_i += 1

        return result_min