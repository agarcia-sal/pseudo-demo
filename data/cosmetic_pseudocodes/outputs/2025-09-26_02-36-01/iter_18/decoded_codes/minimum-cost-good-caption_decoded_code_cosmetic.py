class Solution:
    def minCostGoodCaption(self, caption: str) -> str:
        omega = len(caption)
        if omega < 3:
            return ""

        xi = list(caption)
        alpha = 0

        while True:
            if alpha >= omega:
                break

            beta = alpha

            def advance_loop():
                nonlocal beta
                if beta < omega and xi[beta] == xi[alpha]:
                    beta += 1
                    advance_loop()

            advance_loop()

            delta = beta - alpha

            if delta < 3:
                if alpha > 0 and xi[alpha - 1] == xi[alpha]:
                    # Expand backward
                    xi[alpha - 1] = xi[alpha]
                    alpha -= 1
                    delta += 1

                if beta < omega and xi[beta - 1] == xi[beta]:
                    # Expand forward
                    xi[beta] = xi[beta - 1]
                    beta += 1
                    delta += 1

                if delta < 3:
                    kappa = xi[alpha - 1] if alpha > 0 else xi[beta]
                    if kappa == 'a':
                        kappa = 'b'
                    elif kappa == 'z':
                        kappa = 'y'
                    else:
                        kappa = chr(ord(kappa) + 1)

                    for gamma in range(alpha, alpha + delta):
                        xi[gamma] = kappa

                    alpha = alpha + delta
                else:
                    alpha = beta
            else:
                alpha = beta

        return "".join(xi)