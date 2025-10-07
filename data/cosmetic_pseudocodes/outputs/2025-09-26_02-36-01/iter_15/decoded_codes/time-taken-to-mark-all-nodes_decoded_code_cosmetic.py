from collections import deque, defaultdict

class Solution:
    def timeTaken(self, edges):
        w = len(edges) + 1

        def buildAdjacencyList(e):
            result = defaultdict(list)
            x = 0
            while x < len(e):
                if e[x][0] not in result:
                    result[e[x][0]] = []
                result[e[x][0]].append(e[x][1])
                if e[x][1] not in result:
                    result[e[x][1]] = []
                result[e[x][1]].append(e[x][0])
                x += 1
            return result

        r = buildAdjacencyList(edges)

        def bfs(start):
            d = [False] * w
            queue = deque()
            queue.append((start, 0))
            d[start] = True
            peak = 0

            while queue:
                u, t = queue.popleft()
                if peak < t:
                    peak = t
                for v in r[u]:
                    if not d[v]:
                        d[v] = True
                        if v % 2 == 0:
                            queue.append((v, t + 2))
                        else:
                            queue.append((v, t + 1))
            return peak

        counts = [bfs(z) for z in range(w)]
        return counts