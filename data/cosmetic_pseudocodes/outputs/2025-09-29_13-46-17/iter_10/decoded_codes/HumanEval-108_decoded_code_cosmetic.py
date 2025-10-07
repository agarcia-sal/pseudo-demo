from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        sign: int = 1
        if integer_value < 0:
            integer_value = -integer_value
            sign = -1

        digits: List[int] = [int(ch) for ch in str(integer_value)]
        transformed: List[int] = []

        def rec_mul_head(lst: List[int], idx: int, factor: int) -> None:
            if idx == 0:
                transformed.append(lst[0] * factor)
            else:
                transformed.append(lst[idx])
            if idx + 1 < len(lst):
                rec_mul_head(lst, idx + 1, factor)

        rec_mul_head(digits, 0, sign)

        def rec_sum(lst: List[int], pos: int, acc: int) -> int:
            if pos == len(lst):
                return acc
            return rec_sum(lst, pos + 1, acc + lst[pos])

        return rec_sum(transformed, 0, 0)

    def fold_digits_sum(lst: List[int], idx: int, acc: List[int]) -> List[int]:
        if idx == len(lst):
            return acc
        return fold_digits_sum(lst, idx + 1, acc + [digits_sum(lst[idx])])

    omega_eta: List[int] = fold_digits_sum(array_of_integers, 0, [])

    def incompatible_filter(lst: List[int], idx: int, acc_out: List[int]) -> List[int]:
        if idx == len(lst):
            return acc_out
        if lst[idx] > 0:
            return incompatible_filter(lst, idx + 1, acc_out + [lst[idx]])
        else:
            return incompatible_filter(lst, idx + 1, acc_out)

    rho_psi_one: List[int] = incompatible_filter(omega_eta, 0, [])

    return len(rho_psi_one)