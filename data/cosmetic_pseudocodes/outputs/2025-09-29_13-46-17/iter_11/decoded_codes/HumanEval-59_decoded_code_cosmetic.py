from typing import List

def largest_prime_factor(n: int) -> int:
    def is_prime(k: int) -> bool:
        def recursive_check(index: int) -> bool:
            if index > k - 1:
                return True
            if k % index == 0:
                return False
            return recursive_check(index + 1)
        return k >= 2 and recursive_check(2)

    def fold_divisors(lst: List[int], acc: int) -> int:
        if not lst:
            return acc
        head, tail = lst[0], lst[1:]
        updated_acc = max(acc, head) if (n % head == 0 and is_prime(head)) else acc
        return fold_divisors(tail, updated_acc)

    return fold_divisors(list(range(2, n + 1)), 1)