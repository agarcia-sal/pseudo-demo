from bisect import bisect_left

class Fenwick:
    def __init__(self, u):
        self.tree = [0] * (u + 1)

    def add(self, j):
        k = j
        while k < len(self.tree):
            self.tree[k] += 1
            k += k & (-k)

    def pre(self, v):
        acc = 0
        while v > 0:
            acc += self.tree[v]
            v &= v - 1
        return acc

    def query(self, a, b):
        return self.pre(b) - self.pre(a - 1)

class Solution:
    def maxRectangleArea(self, alpha, beta):
        pairedList = sorted((alpha[p], beta[p]) for p in range(len(alpha)))
        uniqueYs = sorted(set(beta))
        maximumArea = -1
        fenw = Fenwick(len(uniqueYs))
        fenw.add(bisect_left(uniqueYs, pairedList[0][1]) + 1)
        priorMap = {}

        for idx in range(len(pairedList) - 1):
            mux1, muy1 = pairedList[idx]
            mux2, muy2 = pairedList[idx + 1]
            mappedY = bisect_left(uniqueYs, muy2) + 1
            fenw.add(mappedY)
            if mux1 != mux2:
                continue

            currentVal = fenw.query(bisect_left(uniqueYs, muy1) + 1, mappedY)

            if muy2 in priorMap and priorMap[muy2][1] == muy1 and priorMap[muy2][2] + 2 == currentVal:
                maximumArea = max(maximumArea, (mux2 - priorMap[muy2][0]) * (muy2 - muy1))

            priorMap[muy2] = (mux1, muy1, currentVal)

        return maximumArea