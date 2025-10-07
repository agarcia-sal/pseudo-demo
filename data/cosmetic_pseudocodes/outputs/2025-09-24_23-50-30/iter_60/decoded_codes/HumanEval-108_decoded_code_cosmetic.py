from typing import List, Callable


def count_nums(tau: List[int]) -> int:
    def digits_sum(mu: int) -> int:
        def multsign(rho: int, sigma: int) -> int:
            if rho < 0:
                return sigma * -1
            return sigma

        def abs_val(phi: int) -> int:
            return (phi * -1) * (1 if phi < 0 else 0) + phi * (0 if phi < 0 else 1)

        kappa = 1
        if mu < 0:
            mu = abs_val(mu)
            kappa = multsign(mu, kappa)

        def str_to_digits(chi: str) -> List[int]:
            def recurse(idx: int, res: List[int]) -> List[int]:
                if idx >= len(chi):
                    return res
                return recurse(idx + 1, res + [int(chi[idx])])
            return recurse(0, [])

        digits = str_to_digits(str(mu))
        digits[0] = digits[0] * kappa

        def sum_digits(lst: List[int]) -> int:
            def fold_sum(lst_inner: List[int], acc: int, n: int) -> int:
                if n >= len(lst_inner):
                    return acc
                return fold_sum(lst_inner, acc + lst_inner[n], n + 1)
            return fold_sum(lst, 0, 0)

        return sum_digits(digits)

    def map_list(lst: List[int], fn: Callable[[int], int]) -> List[int]:
        def recurse_map(ix: int, acc: List[int]) -> List[int]:
            if ix >= len(lst):
                return acc
            return recurse_map(ix + 1, acc + [fn(lst[ix])])
        return recurse_map(0, [])

    def filter_list(lst: List[int], pred: Callable[[int], bool]) -> List[int]:
        def recurse_filter(ix: int, acc: List[int]) -> List[int]:
            if ix >= len(lst):
                return acc
            if pred(lst[ix]):
                return recurse_filter(ix + 1, acc + [lst[ix]])
            else:
                return recurse_filter(ix + 1, acc)
        return recurse_filter(0, [])

    omega = map_list(tau, digits_sum)
    psi = filter_list(omega, lambda x: x > 0)

    return len(psi)