class Solution:
    def minEnd(self, n: int, x: int) -> int:
        def canConstruct(max_val: int) -> bool:
            alpha = x
            beta = 1
            while True:
                if not (alpha < max_val):
                    break
                alpha += 1
                temp_flag = (alpha & x) == x
                if temp_flag:
                    beta += 1
                    if beta == n:
                        return True
            return beta == n

        lambda_ = x
        mu = 2000000000  # 2 * 5 * 10^7 as given
        while lambda_ < mu:
            nu = lambda_ + mu
            xi = nu // 2  # integer division
            omega = xi
            psi = omega
            if canConstruct(psi):
                mu = psi
            else:
                lambda_ += 1
        return lambda_