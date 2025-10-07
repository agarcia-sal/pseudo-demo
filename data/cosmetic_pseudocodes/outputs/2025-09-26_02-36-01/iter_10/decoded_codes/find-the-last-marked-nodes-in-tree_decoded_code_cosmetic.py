from typing import List

class Solution:
    def lastMarkedNodes(self, edges: List[List[int]]) -> List[int]:
        m = len(edges) + 1
        g: List[List[int]] = []

        def initGraph(i: int) -> None:
            if i < m:
                g.append([])
                initGraph(i + 1)
        initGraph(0)

        def buildGraph(i: int) -> None:
            if i >= len(edges):
                return
            u, v = edges[i]
            g[u].append(v)
            g[v].append(u)
            buildGraph(i + 1)
        buildGraph(0)

        def fillList(l: List[int], val: int, idx: int) -> None:
            if idx == m:
                return
            l[idx] = val
            fillList(l, val, idx + 1)

        def dfs(t: int, p: int, d: List[int]) -> None:
            # The while True only runs once and breaks immediately; so simplified
            def recur(q: int, r: int) -> None:
                if r == t:
                    return
                def innerLoop(lst: List[int], idx: int) -> None:
                    if idx >= len(lst):
                        return
                    if lst[idx] != r:
                        d[lst[idx]] = d[r] + 1
                        recur(lst[idx], r)
                    innerLoop(lst, idx + 1)
                innerLoop(g[t], 0)
            recur(t, p)

        dist1 = [-1] * m
        dist1[0] = 0
        dfs(0, -1, dist1)

        def maxPos(arr: List[int], idx: int, curMax: int, curPos: int) -> int:
            if idx == len(arr):
                return curPos
            if arr[idx] > curMax:
                return maxPos(arr, idx + 1, arr[idx], idx)
            else:
                return maxPos(arr, idx + 1, curMax, curPos)

        a = maxPos(dist1, 0, float('-inf'), -1)

        dist2 = [-1] * m
        dist2[a] = 0
        dfs(a, -1, dist2)

        b = maxPos(dist2, 0, float('-inf'), -1)

        dist3 = [-1] * m
        dist3[b] = 0
        dfs(b, -1, dist3)

        res: List[int] = []
        def buildRes(xi: int, yi: int) -> None:
            if xi == len(dist2):
                return
            if dist2[xi] > dist3[yi]:
                res.append(a)
            else:
                res.append(b)
            buildRes(xi + 1, yi + 1)
        buildRes(0, 0)

        return res