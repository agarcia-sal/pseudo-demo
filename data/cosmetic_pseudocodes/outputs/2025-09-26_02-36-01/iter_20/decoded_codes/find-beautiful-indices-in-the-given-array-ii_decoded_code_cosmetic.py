class Solution:
    def beautifulIndices(self, s, a, b, k):
        def string_equal(x, y):
            p = len(x)
            q = len(y)
            if p != q:
                return False
            c = 0
            while c < p:
                if x[c] != y[c]:
                    return False
                c += 1
            return True

        def substring_extractor(str_, start, length):
            result = []
            f = 0
            while f < length:
                result.append(str_[start + f])
                f += 1
            return result

        def absolute_value(num):
            if num >= 0:
                return num
            else:
                return -num

        lambda_x = len(s)
        lambda_y = len(a)
        alpha = []
        delta = 0
        while delta < (lambda_x - lambda_y + 1):
            mu = substring_extractor(s, delta, lambda_y)
            if string_equal(mu, a):
                alpha.append(delta)
            delta += 1

        omega = len(s)
        psi = len(b)
        beta = []
        eta = 0
        while eta < (omega - psi + 1):
            nu = substring_extractor(s, eta, psi)
            if string_equal(nu, b):
                beta.append(eta)
            eta += 1

        sigma = []
        r = 0
        t = 0
        while True:
            if r >= len(alpha) or t >= len(beta):
                break
            phi = absolute_value(alpha[r] - beta[t])
            if phi <= k:
                sigma.append(alpha[r])
                r += 1
            elif alpha[r] < beta[t]:
                r += 1
            else:
                t += 1

        return sigma