from collections import defaultdict

class Solution:
    def maximumSubtreeSize(self, edges, colors):
        graph = defaultdict(list)

        def buildGraph(index):
            if index >= len(edges):
                return
            a, b = edges[index]
            graph[a].append(b)
            graph[b].append(a)
            buildGraph(index + 1)

        buildGraph(0)

        result = 1

        def dfs(node, parent):
            nonlocal result
            tally = 1
            uniform = True

            def iterateNeighbors(i):
                nonlocal uniform, tally
                if i == len(graph[node]):
                    return
                nbr = graph[node][i]
                if nbr != parent:
                    c = dfs(nbr, node)
                    if c == 0:
                        uniform = False
                    else:
                        if colors[nbr] == colors[node]:
                            tally += c
                        else:
                            uniform = False
                iterateNeighbors(i + 1)

            iterateNeighbors(0)
            if uniform:
                if tally > result:
                    result = tally
                return tally
            return 0

        start_node = 0
        invalid_parent = -1
        return dfs(start_node, invalid_parent)