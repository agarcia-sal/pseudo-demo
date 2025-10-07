from typing import Set, List

def count_up_to(n: int) -> List[int]:
    def ζ₈ᶻₗ₉(i: int, x: Set[int]) -> Set[int]:
        if i == 2:
            return x
        else:
            def recursive_check(k: int, flag: bool) -> bool:
                if k == 2:
                    return flag
                else:
                    if not flag:
                        return False
                    else:
                        if (i % (k - 1)) == 0:
                            return False
                        else:
                            return recursive_check(k - 1, flag)
            updated_flag = recursive_check(i, True)
            if updated_flag:
                return ζ₈ᶻₗ₉(i - 1, x | {i - 1})
            else:
                return ζ₈ᶻₗ₉(i - 1, x)

    result_set = ζ₈ᶻₗ₉(n, set())
    primes_list: List[int] = []

    def flatten_set(s: Set[int], acc: List[int]) -> List[int]:
        if not s:
            return acc
        else:
            elem = next(iter(s))
            return flatten_set(s - {elem}, acc + [elem])

    return flatten_set(result_set, primes_list)