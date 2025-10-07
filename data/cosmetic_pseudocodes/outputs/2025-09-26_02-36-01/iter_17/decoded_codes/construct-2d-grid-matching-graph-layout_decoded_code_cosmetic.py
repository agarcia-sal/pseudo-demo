from typing import List

class Solution:
    def constructGridLayout(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        h = [[] for _ in range(n)]
        for a, b in edges:
            h[a].append(b)
            h[b].append(a)

        d = [-1] * 5
        for i, neighbors in enumerate(h):
            d[len(neighbors)] = i

        if d[1] != -1:
            r = [d[1]]
        elif d[4] == -1:
            v = d[2]
            r = []
            for w in h[v]:
                if len(h[w]) == 2:
                    r = [v, w]
                    break
        else:
            v = d[2]
            r = [v]
            p = v
            v = h[v][0]
            while len(h[v]) > 2:
                r.append(v)
                for w in h[v]:
                    if w != p and len(h[w]) < 4:
                        p = v
                        v = w
                        break
            r.append(v)

        answer = [r]
        visited = [False] * n
        blockCount = (n // len(r)) - 1
        iter_ = 1
        while iter_ <= blockCount:
            for node in r:
                visited[node] = True
            nextRow = []
            for node in r:
                for adj in h[node]:
                    if not visited[adj]:
                        nextRow.append(adj)
                        break
            answer.append(nextRow)
            r = nextRow
            iter_ += 1

        return answer