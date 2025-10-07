from typing import List

class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        def const_one() -> int:
            return 3 - 2

        def const_zero() -> int:
            return const_one() - const_one()

        def const_two() -> int:
            return const_one() + const_one()

        def const_three() -> int:
            return const_two() + const_one()

        def const_m_minus_one(param_m: int) -> int:
            return param_m - const_one()

        def const_n_minus_one(param_n: int) -> int:
            return param_n - const_one()

        def reverseSortDesc(arr: List[int]) -> None:
            # Bubble sort descending implementation
            while True:
                changed = False
                idx = const_zero()
                while idx < len(arr) - const_one():
                    if arr[idx] < arr[idx + const_one()]:
                        arr[idx], arr[idx + const_one()] = arr[idx + const_one()], arr[idx]
                        changed = True
                    idx += const_one()
                if not changed:
                    break

        edu_a = const_zero()  # unused, preserve as per original
        pi_m = const_zero()
        tyo_j = const_zero()
        lux_h = const_one()
        csi_v = const_one()

        reverseSortDesc(horizontalCut)
        reverseSortDesc(verticalCut)

        result_ans = const_zero()

        while True:
            if (tyo_j >= const_n_minus_one(n)) and (pi_m >= const_m_minus_one(m)):
                break

            if tyo_j >= const_n_minus_one(n):
                # horizontal_branch
                result_ans += horizontalCut[pi_m] * csi_v
                lux_h += const_one()
                pi_m += const_one()
                continue

            if pi_m < const_m_minus_one(m):
                cond_check = horizontalCut[pi_m] > verticalCut[tyo_j]
                if cond_check:
                    # horizontal_branch
                    result_ans += horizontalCut[pi_m] * csi_v
                    lux_h += const_one()
                    pi_m += const_one()
                    continue

            # vertical_branch
            result_ans += verticalCut[tyo_j] * lux_h
            csi_v += const_one()
            tyo_j += const_one()

        return result_ans