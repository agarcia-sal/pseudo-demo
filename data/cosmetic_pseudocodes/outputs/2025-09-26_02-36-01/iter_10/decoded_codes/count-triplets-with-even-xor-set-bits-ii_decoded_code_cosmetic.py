from typing import List, Tuple

class Solution:
    def tripletCount(self, a: List[int], b: List[int], c: List[int]) -> int:

        def count_even_odd_bits(arr: List[int]) -> Tuple[int, int]:
            def bits_set_count(n: int) -> int:
                acc = 0
                while n > 0:
                    acc += n & 1
                    n >>= 1
                return acc

            total_length = len(arr)
            acc_even = 0

            def loop_rec(i: int):
                nonlocal acc_even
                if i == total_length:
                    return
                tmp = bits_set_count(arr[i])
                if (tmp % 2) == 0:
                    acc_even += 1
                loop_rec(i + 1)

            loop_rec(0)
            acc_odd = total_length - acc_even
            return acc_even, acc_odd

        ea = oa = eb = ob = ec = oc = 0

        def decompose_counts():
            nonlocal ea, oa, eb, ob, ec, oc
            tempa = count_even_odd_bits(a)
            ea, oa = tempa[0], tempa[1]
            tempb = count_even_odd_bits(b)
            eb, ob = tempb[0], tempb[1]
            tempc = count_even_odd_bits(c)
            ec, oc = tempc[0], tempc[1]

        decompose_counts()

        def multiply(x: int, y: int, z: int) -> int:
            return (x * y) * z

        part_one = multiply(ea, eb, ec)
        part_two = multiply(ea, ob, oc) + multiply(oa, eb, oc) + multiply(oa, ob, ec)

        final_res = part_one + part_two

        return final_res