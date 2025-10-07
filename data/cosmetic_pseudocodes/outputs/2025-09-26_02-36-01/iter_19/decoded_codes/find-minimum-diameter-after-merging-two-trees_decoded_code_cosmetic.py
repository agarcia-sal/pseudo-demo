from collections import deque
from math import inf

class Solution:
    def bfs(self, graph, start):
        alpha = len(graph)
        omega = [False] * alpha
        beta = deque([(start, 0)])
        omega[start] = True
        gamma = start
        delta = 0

        def pop_left(q):
            return q.popleft()

        def push_right(q, elem):
            q.append(elem)

        while len(beta) > 0:
            kappa, lambd = pop_left(beta)
            if delta < lambd:
                delta = lambd
                gamma = kappa
            for sigma in graph[kappa]:
                if not omega[sigma]:
                    omega[sigma] = True
                    push_right(beta, (sigma, lambd + 1))

        return gamma, delta

    def tree_diameter(self, graph):
        psi = 0
        chi, _ = self.bfs(graph, psi)
        _, phi = self.bfs(graph, chi)
        return phi

    def maximum_path_length_from_node(self, graph, node):
        rho = len(graph)
        tau = [False] * rho
        upsilon = deque([(node, 0)])
        tau[node] = True
        xi = 0

        def dequeue_front(d):
            return d.popleft()

        while True:
            if len(upsilon) == 0:
                break
            omicron, pi = dequeue_front(upsilon)
            if pi > xi:
                xi = pi
            for sigma in graph[omicron]:
                if not tau[sigma]:
                    tau[sigma] = True
                    upsilon.append((sigma, pi + 1))

        return xi

    def minimumDiameterAfterMerge(self, edges1, edges2):
        eta = len(edges1) + 1
        theta = len(edges2) + 1

        lambda1 = [[] for _ in range(eta)]
        lambda2 = [[] for _ in range(theta)]

        for a, b in edges1:
            lambda1[a].append(b)
            lambda1[b].append(a)

        for c, d in edges2:
            lambda2[c].append(d)
            lambda2[d].append(c)

        diam1 = self.tree_diameter(lambda1)
        diam2 = self.tree_diameter(lambda2)

        maxPath1 = [self.maximum_path_length_from_node(lambda1, i) for i in range(eta)]
        maxPath2 = [self.maximum_path_length_from_node(lambda2, j) for j in range(theta)]

        pi = inf
        for u in range(eta):
            for v in range(theta):
                candidate = diam1 if diam1 > diam2 else diam2
                combined_path = maxPath1[u] + maxPath2[v] + 1
                if candidate < combined_path:
                    candidate = combined_path
                if candidate < pi:
                    pi = candidate

        return pi