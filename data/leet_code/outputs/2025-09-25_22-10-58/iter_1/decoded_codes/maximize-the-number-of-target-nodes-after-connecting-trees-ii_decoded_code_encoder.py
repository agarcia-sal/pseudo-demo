from collections import defaultdict, deque

class Solution:
    def maxTargetNodes(self, edges1, edges2):
        adj1 = defaultdict(list)
        adj2 = defaultdict(list)

        for u, v in edges1:
            adj1[u].append(v)
            adj1[v].append(u)

        for u, v in edges2:
            adj2[u].append(v)
            adj2[v].append(u)

        # number of nodes as number of distinct keys in the adjacency dictionaries
        n = len(adj1)
        m = len(adj2)

        def bfs(tree, start):
            even_count = 0
            odd_count = 0
            queue = deque([(start, 0)])
            visited = {start}

            while queue:
                node, dist = queue.popleft()
                if dist % 2 == 0:
                    even_count += 1
                else:
                    odd_count += 1

                for neighbor in tree[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, dist + 1))
            return even_count, odd_count

        even_odd_counts_1 = [bfs(adj1, i) for i in range(n)]
        even_odd_counts_2 = [bfs(adj2, i) for i in range(m)]

        result = []
        for i in range(n):
            even_count_1, _ = even_odd_counts_1[i]
            max_targets = 0
            for j in range(m):
                even_count_2, odd_count_2 = even_odd_counts_2[j]
                if i == j or (i % 2) == (j % 2):
                    targets_if_connected_to_j = even_count_2
                else:
                    targets_if_connected_to_j = odd_count_2

                if targets_if_connected_to_j > max_targets:
                    max_targets = targets_if_connected_to_j
            result.append(even_count_1 + max_targets)

        return result