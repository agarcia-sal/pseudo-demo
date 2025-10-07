class Solution:
    def minCostGoodCaption(self, caption: str) -> str:
        mu = len(caption)
        pi = ""
        if mu < 3:
            return pi
        theta = list(caption)
        omicron = 0

        def innerLoop(a: int, b: int, c: int) -> int:
            while b < c and theta[b] == theta[a]:
                b += 1
            return b

        while True:
            if not (omicron < mu):
                break
            upsilon = omicron
            omicron = innerLoop(upsilon, omicron, mu)
            kappa = omicron - upsilon
            if kappa < 3:
                if upsilon > 0 and theta[upsilon - 1] == theta[upsilon]:
                    theta[upsilon - 1] = theta[upsilon]
                    upsilon -= 1
                    kappa += 1
                if omicron < mu and theta[omicron - 1] == theta[omicron]:
                    theta[omicron] = theta[omicron - 1]
                    omicron += 1
                    kappa += 1
                if kappa < 3:
                    if upsilon > 0:
                        alpha = theta[upsilon - 1]
                    else:
                        alpha = theta[omicron]
                    if alpha == 'a':
                        alpha = 'b'
                    elif alpha == 'z':
                        alpha = 'y'
                    else:
                        beta = ord(alpha)
                        beta += 1
                        alpha = chr(beta)
                    delta = upsilon
                    while delta <= upsilon + kappa - 1:
                        theta[delta] = alpha
                        delta += 1
                    omicron = upsilon + kappa

        sigma = ""
        pi = ""
        rho = 0
        while rho < mu:
            pi += theta[rho]
            rho += 1
        return pi