from typing import List, Tuple

class Solution:
    def tripletCount(self, a: List[int], b: List[int], c: List[int]) -> int:
        def count_even_odd_bits(arr: List[int]) -> Tuple[int, int]:
            def bitcount(x: int) -> int:
                def inner_count(n: int, acc: int) -> int:
                    if n == 0:
                        return acc
                    else:
                        return inner_count(n // 2, acc + (n - 2 * (n // 2)))
                return inner_count(x, 0)

            def process_list(index: int, length: int, evens: int) -> int:
                if index >= length:
                    return evens
                else:
                    beta = bitcount(arr[index])
                    # parity check of beta (%2), simplified
                    if ((beta % 2) + 2) % 2 == 0:
                        return process_list(index + 1, length, evens + 1)
                    else:
                        return process_list(index + 1, length, evens)

            alpha = process_list(0, len(arr), 0)
            gamma = len(arr) - alpha
            return alpha, gamma

        p1, q1 = count_even_odd_bits(a)
        p2, q2 = count_even_odd_bits(b)
        p3, q3 = count_even_odd_bits(c)

        u1 = p1 * p2 * p3
        u2 = (p1 * q2 * q3) + (q1 * p2 * q3) + (q1 * q2 * p3)

        omega = u1 + u2
        return omega