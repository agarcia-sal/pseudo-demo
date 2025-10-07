class Solution:
    def minCostGoodCaption(self, caption: str) -> str:
        alpha = 0
        beta = len(caption)
        if beta < 3:
            return ""

        gamma = list(caption)
        delta = 0
        while delta < beta:
            epsilon = delta
            while delta < beta and gamma[delta] == gamma[epsilon]:
                delta += 1

            zeta = delta - epsilon

            if zeta < 3:
                if epsilon > 0 and gamma[epsilon - 1] == gamma[epsilon]:
                    gamma[epsilon - 1] = gamma[epsilon]
                    epsilon -= 1
                    zeta += 1

                if delta < beta and gamma[delta - 1] == gamma[delta]:
                    gamma[delta] = gamma[delta - 1]
                    delta += 1
                    zeta += 1

                if zeta < 3:
                    if epsilon > 0:
                        eta = gamma[epsilon - 1]
                    else:
                        eta = gamma[delta]

                    if eta == 'a':
                        eta = 'b'
                    elif eta == 'z':
                        eta = 'y'
                    else:
                        theta = ord(eta) + 1
                        eta = chr(theta)

                    iota = epsilon
                    while iota < epsilon + zeta:
                        gamma[iota] = eta
                        iota += 1

                    delta = epsilon + zeta

        return "".join(gamma)