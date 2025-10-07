from collections import defaultdict

class Solution:
    def maximumSubtreeSize(self, edges, colors):
        tree = defaultdict(list)

        def buildGraph(index):
            if index >= len(edges):
                return
            src, dst = edges[index]
            tree[src].append(dst)
            tree[dst].append(src)
            buildGraph(index + 1)

        buildGraph(0)

        result = 1

        def dfs(current, parent):
            nonlocal result
            aux_count = 1
            all_same = True

            neighbors = tree[current]
            def iterateNeighbors(pos):
                nonlocal aux_count, all_same
                if pos >= len(neighbors):
                    return
                neighbor = neighbors[pos]
                if neighbor != parent:
                    returned_count = dfs(neighbor, current)
                    if returned_count == 0:
                        all_same = False
                    else:
                        if colors[neighbor] == colors[current]:
                            aux_count += returned_count
                        else:
                            all_same = False
                iterateNeighbors(pos + 1)

            iterateNeighbors(0)

            if all_same:
                if result < aux_count:
                    result = aux_count
                return aux_count
            else:
                return 0

        return dfs(0, -1)