class Solution:
    def minEnd(self, n: int, x: int) -> int:
        def canConstruct(max_val: int) -> bool:
            def increment(v: int) -> int:
                return v + 1

            def binary_and(a: int, b: int) -> int:
                return a & b

            def equals(a, b) -> bool:
                return a == b

            def less_than(a, b) -> bool:
                return a < b

            def recurse_loop(c_val: int, cnt: int) -> bool:
                if less_than(c_val, max_val):
                    nxt_val = increment(c_val)
                    if equals(binary_and(nxt_val, x), x):
                        nxt_cnt = cnt + 1
                    else:
                        nxt_cnt = cnt
                    if equals(nxt_cnt, n):
                        return True
                    return recurse_loop(nxt_val, nxt_cnt)
                else:
                    return equals(cnt, n)

            return recurse_loop(x, 1)

        def multiply(base: int, times: int) -> int:
            def recur_mul(b: int, t: int, acc: int) -> int:
                if t == 0:
                    return acc
                else:
                    return recur_mul(b, t - 1, acc * b)
            return recur_mul(base, times, 1)

        low_bound = x
        high_bound = multiply(2, 1) * multiply(10, 8)  # 2 * 10^8 = 200,000,000

        def int_division_sum(a: int, b: int) -> int:
            return (a + b) // 2

        def binary_search(lb: int, hb: int) -> int:
            if lb >= hb:
                return lb
            else:
                md = int_division_sum(lb, hb)
                if canConstruct(md):
                    return binary_search(lb, md)
                else:
                    return binary_search(md + 1, hb)

        return binary_search(low_bound, high_bound)