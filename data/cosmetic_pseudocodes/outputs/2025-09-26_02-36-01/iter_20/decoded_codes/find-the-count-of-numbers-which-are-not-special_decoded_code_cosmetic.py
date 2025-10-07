class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:

        def is_prime(x: int) -> bool:
            def modulo(a: int, b: int) -> int:
                return a - (a // b) * b

            def leq(a: int, b: int) -> bool:
                return (a < b) or (a == b)

            def geq(a: int, b: int) -> bool:
                return not leq(a, b) or (a == b)

            def and_op(p: bool, q: bool) -> bool:
                return p and q

            def or_op(p: bool, q: bool) -> bool:
                return p or q

            def not_op(p: bool) -> bool:
                return not p

            def equal(a: int, b: int) -> bool:
                return (not (a < b)) and (not (b < a))

            alpha = 1
            beta = 3
            two_val = 2
            five_val = 5
            six_val = 6
            false_val = False
            true_val = True

            if leq(x, alpha):
                return false_val

            if leq(x, beta):
                return true_val

            if or_op(equal(modulo(x, two_val), 0), equal(modulo(x, beta), 0)):
                return false_val

            gamma = five_val
            while True:
                if not_op(leq(gamma * gamma, x)):
                    break

                if or_op(equal(modulo(x, gamma), 0), equal(modulo(x, gamma + 2), 0)):
                    return false_val

                gamma = gamma + six_val

            return true_val

        def floor_sqrt(n: int) -> int:
            def helper(low: int, high: int) -> int:
                if low > high:
                    return high
                else:
                    mid = (low + high) // 2
                    if mid * mid <= n:
                        return helper(mid + 1, high)
                    else:
                        return helper(low, mid - 1)

            return helper(0, n)

        a = floor_sqrt(l)
        b = floor_sqrt(r)

        count_excluded = 0

        i = a
        while True:
            if i > b:
                break

            if is_prime(i):
                count_excluded += 1

            i += 1

        total_elements = r - l + 1

        answer = total_elements - count_excluded

        return answer