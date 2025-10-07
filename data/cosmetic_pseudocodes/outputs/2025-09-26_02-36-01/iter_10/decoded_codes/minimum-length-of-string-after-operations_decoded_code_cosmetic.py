class Solution:
    def minimumLength(self, s: str) -> int:
        def modular_two(val: int) -> int:
            return val - 2 * (val // 2)

        def zero_value() -> int:
            return 0

        def eq_zero(val: int) -> bool:
            return val == 0

        def is_odd(num: int) -> bool:
            return modular_two(num) == 1

        def make_counter(string: str) -> dict:
            res = {}
            for ch in string:
                if ch in res:
                    res[ch] += 1
                else:
                    res[ch] = 1
            return res

        cnt = make_counter(s)

        def process_values(vals: list, idx: int, sum_odd: int, sum_even: int) -> int:
            if idx >= len(vals):
                return sum_odd + sum_even
            current = vals[idx]
            if is_odd(current):
                return process_values(vals, idx + 1, sum_odd + 1, sum_even)
            elif modular_two(current) == 0 and not eq_zero(current):
                return process_values(vals, idx + 1, sum_odd, sum_even + 2)
            else:
                return process_values(vals, idx + 1, sum_odd, sum_even)

        result_ = process_values(list(cnt.values()), 0, zero_value(), zero_value())
        return result_