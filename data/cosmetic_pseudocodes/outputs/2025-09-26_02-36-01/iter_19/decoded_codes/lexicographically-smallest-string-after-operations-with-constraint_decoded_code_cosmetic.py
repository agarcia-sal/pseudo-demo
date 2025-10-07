class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        def cyclic_distance(x: str, y: str) -> int:
            u = abs(ord(x) - ord(y))
            v = 26 - u
            return u if u <= v else v

        omega = len(s)
        delta = 0
        phi = list(s)
        lambda_ = k

        while lambda_ > 0 and delta < omega:
            if phi[delta] == 'a':
                delta += 1
                continue

            rho = cyclic_distance(phi[delta], 'a')
            if rho <= lambda_:
                phi[delta] = 'a'
                lambda_ -= rho
            else:
                temp_code = ord(phi[delta]) - lambda_
                phi[delta] = chr(temp_code)
                lambda_ = 0

            delta += 1

        return ''.join(phi)