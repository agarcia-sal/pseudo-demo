from typing import List

class Solution:
    def lastMarkedNodes(self, edges: List[List[int]]) -> List[int]:
        def dfs(w: int, p: int, measures: List[int]) -> None:
            idx = 0
            while idx < len(g[w]):
                nb = g[w][idx]
                if nb != p:
                    measures[nb] = measures[w] + 1
                    dfs(nb, w, measures)
                idx += 1

        nodeCount = len(edges) + 1
        g = [[] for _ in range(nodeCount)]

        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        measuresOne = [-1] * nodeCount
        measuresOne[0] = 0
        dfs(0, -1, measuresOne)

        maxPosA = 0
        for i in range(1, nodeCount):
            if measuresOne[i] > measuresOne[maxPosA]:
                maxPosA = i

        measuresTwo = [-1] * nodeCount
        measuresTwo[maxPosA] = 0
        dfs(maxPosA, -1, measuresTwo)

        maxPosB = 0
        for i in range(1, nodeCount):
            if measuresTwo[i] > measuresTwo[maxPosB]:
                maxPosB = i

        measuresThree = [-1] * nodeCount
        measuresThree[maxPosB] = 0
        dfs(maxPosB, -1, measuresThree)

        outputList = []
        for i in range(nodeCount):
            valOne = measuresTwo[i]
            valTwo = measuresThree[i]
            if valOne > valTwo:
                outputList.append(maxPosA)
            else:
                outputList.append(maxPosB)

        return outputList