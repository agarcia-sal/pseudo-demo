from typing import List

class Solution:
    def lastMarkedNodes(self, edges: List[List[int]]) -> List[int]:

        def dfs(p: int, q: int, r: List[int]) -> None:
            def rec(s: List[int], t: int, u: int) -> None:
                if u < len(s):
                    v = s[u]
                    if v != t:
                        r[v] = r[p] + 1
                        rec(s, t, u + 1)
                    else:
                        rec(s, t, u + 1)
            rec(g[p], q, 0)

        x = len(edges) + 1

        def genList(n: int) -> List[List[int]]:
            if n <= 0:
                return []
            else:
                return [[]] + genList(n - 1)

        g: List[List[int]] = genList(x)

        def addEdges(lst: List[List[int]], idx1: int, idx2: int) -> None:
            if lst == []:
                return
            else:
                top = lst[0]
                rest = lst[1:]
                r_idx = idx1
                s_idx = idx2
                g[r_idx].append(s_idx)
                g[s_idx].append(r_idx)
                addEdges(rest, r_idx, s_idx)

        def buildEdges(e: List[List[int]], k: int) -> None:
            if k < len(e):
                edge = e[k]
                g[edge[0]].append(edge[1])
                g[edge[1]].append(edge[0])
                buildEdges(e, k + 1)

        buildEdges(edges, 0)

        def initList(length: int, val: int) -> List[int]:
            if length <= 0:
                return []
            else:
                return [val] + initList(length - 1, val)

        dist1 = initList(x, -1)
        dist1[0] = 0
        dfs(0, -1, dist1)

        def maxPos(arr: List[int]) -> int:
            def aux(idx: int, maxIndex: int, maxVal: int) -> int:
                if idx >= len(arr):
                    return maxIndex
                if arr[idx] > maxVal:
                    return aux(idx + 1, idx, arr[idx])
                else:
                    return aux(idx + 1, maxIndex, maxVal)
            return aux(0, 0, arr[0])

        a = maxPos(dist1)

        dist2 = initList(x, -1)
        dist2[a] = 0
        dfs(a, -1, dist2)
        b = maxPos(dist2)

        dist3 = initList(x, -1)
        dist3[b] = 0
        dfs(b, -1, dist3)

        result: List[int] = []

        def combineLists(l1: List[int], l2: List[int], idx: int) -> None:
            if idx >= len(l1):
                return
            if l1[idx] > l2[idx]:
                result.append(a)
            else:
                result.append(b)
            combineLists(l1, l2, idx + 1)

        combineLists(dist2, dist3, 0)

        return result