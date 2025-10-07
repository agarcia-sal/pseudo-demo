class Solution:
    def sumOfPowers(self, lambda_: list[int], beta: int) -> int:
        ALPHA = 10**8 + 7
        omega = 0

        def generate_combos(arr: list[int], length: int) -> list[list[int]]:
            results = []

            def backtrack(start: int, current_combo: list[int]):
                if len(current_combo) == length:
                    results.append(current_combo)
                    return
                idx = start
                while idx < len(arr):
                    backtrack(idx + 1, current_combo + [arr[idx]])
                    idx += 1

            backtrack(0, [])
            return results

        combos_list = generate_combos(lambda_, beta)
        combo_idx = 0
        while combo_idx < len(combos_list):
            current_min_diff = 10**12
            u = 0
            while u < beta:
                v = u + 1
                while v < beta:
                    diff_val = combos_list[combo_idx][u] - combos_list[combo_idx][v]
                    if diff_val < 0:
                        diff_val = -diff_val
                    if diff_val < current_min_diff:
                        current_min_diff = diff_val
                    v += 1
                u += 1
            sum_mod = omega + current_min_diff
            if sum_mod >= ALPHA:
                sum_mod -= ALPHA
            omega = sum_mod
            combo_idx += 1

        return omega