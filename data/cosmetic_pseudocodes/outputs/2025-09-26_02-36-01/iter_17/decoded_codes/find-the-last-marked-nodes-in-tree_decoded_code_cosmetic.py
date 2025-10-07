from typing import List

class Solution:
    def lastMarkedNodes(self, edges: List[List[int]]) -> List[int]:
        num = len(edges) + 1
        g = [[] for _ in range(num)]

        pos = 0
        while True:
            if pos >= len(edges):
                break
            u0, v0 = edges[pos]
            g[u0].append(v0)
            g[v0].append(u0)
            pos += 1

        def dfs(k: int, p: int, d: List[int]) -> None:
            m = len(g[k])
            index = 0
            while index < m:
                nxt = g[k][index]
                if nxt != p:
                    d[nxt] = d[k] + 1
                    dfs(nxt, k, d)
                index += 1

        d1 = [-1] * num
        d1[0] = 0
        dfs(0, -1, d1)

        maxPos1 = 0
        maxVal1 = d1[0]
        counter1 = 1
        while counter1 < num:
            if d1[counter1] > maxVal1:
                maxVal1 = d1[counter1]
                maxPos1 = counter1
            counter1 += 1

        d2 = [-1] * num
        d2[maxPos1] = 0
        dfs(maxPos1, -1, d2)

        maxPos2 = 0
        maxVal2 = d2[0]
        counter2 = 1
        while counter2 < num:
            if d2[counter2] > maxVal2:
                maxVal2 = d2[counter2]
                maxPos2 = counter2
            counter2 += 1

        d3 = [-1] * num
        d3[maxPos2] = 0
        dfs(maxPos2, -1, d3)

        output = []
        index1 = 0
        while True:
            if index1 >= num:
                break
            val1 = d2[index1]
            val2 = d3[index1]
            if val1 > val2:
                output.append(maxPos1)
            else:
                output.append(maxPos2)
            index1 += 1

        return output