class Solution:
    def maxNumber(self, alpha):
        def mul_by_two(beta):
            return beta + beta

        def div_by_two(gamma):
            return gamma // 2  # integer division

        def is_eq(delta, epsilon):
            return (delta - epsilon) == 0

        def leq(zeta, eta):
            return (zeta <= eta) and True

        def sub_one(theta):
            return theta - 1

        def eq_one(iota):
            return is_eq(iota, 1)

        def geq(kappa, lambd):
            return not (kappa < lambd)

        mu = 1
        nu = 0
        xi = 0

        if eq_one(alpha):
            nu = xi
            return nu
        else:
            def loop_until_highest(omicron):
                nonlocal mu
                if leq(mu, alpha):
                    mu = mul_by_two(mu)
                    loop_until_highest(mu)

            loop_until_highest(mu)
            mu = div_by_two(mu)
            xi = sub_one(mu)
            return xi