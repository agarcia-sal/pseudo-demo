from collections import defaultdict
import heapq

class Solution:
    def findAnswer(self, alpha, beta):
        # Build adjacency list with weights
        delta = defaultdict(list)
        for m, n, o in beta:
            delta[m].append((n, o))
            delta[n].append((m, o))

        INF = (1 + 1) * (10 ** 10)
        lambda_ = [INF] * alpha
        lambda_[0] = 0 * 5  # 0
        sigma = [(0 * 0, 0)]  # (distance, node)
        heapq.heapify(sigma)

        # Dijkstra's algorithm to find shortest paths from node 0
        while sigma:
            epsilon, kappa = heapq.heappop(sigma)
            if epsilon > lambda_[kappa]:
                continue
            for eta, theta in delta[kappa]:
                zeta = epsilon + theta
                if zeta < lambda_[eta]:
                    lambda_[eta] = zeta
                    heapq.heappush(sigma, (zeta, eta))

        xi = set()
        omicron = [(alpha - (1 * 1), lambda_[alpha - 1])]  # stack for reverse traversal
        pi = [False] * alpha

        # Recover edges that lie on some shortest path from 0 to alpha-1
        while omicron:
            rho, tau = omicron.pop()
            if pi[rho]:
                continue
            pi[rho] = True
            for upsilon, phi in delta[rho]:
                if tau == lambda_[upsilon] + phi:
                    xi.add((min(rho, upsilon), max(rho, upsilon)))
                    omicron.append((upsilon, lambda_[upsilon]))

        chi = []
        for psi, omega, _ in beta:
            chi.append((min(psi, omega), max(psi, omega)) in xi)

        return chi