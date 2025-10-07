from collections import defaultdict

class Solution:
    def findAnswer(self, n, edges):
        def insertHeap(h, val):
            h.append(val)
            idx = len(h) - 1
            while idx > 0:
                parentIdx = (idx - 1) >> 1
                if h[parentIdx][0] <= h[idx][0]:
                    break
                h[parentIdx], h[idx] = h[idx], h[parentIdx]
                idx = parentIdx

        def popHeap(h):
            result = h[0]
            h[0] = h[-1]
            h.pop()
            pos = 0
            size = len(h)
            while True:
                leftIdx = 2 * pos + 1
                rightIdx = 2 * pos + 2
                smallestIdx = pos
                if leftIdx < size and h[leftIdx][0] < h[smallestIdx][0]:
                    smallestIdx = leftIdx
                if rightIdx < size and h[rightIdx][0] < h[smallestIdx][0]:
                    smallestIdx = rightIdx
                if smallestIdx == pos:
                    break
                h[pos], h[smallestIdx] = h[smallestIdx], h[pos]
                pos = smallestIdx
            return result

        graph = defaultdict(list)
        for e in edges:
            u, v, w = e
            graph[u].append((v, w))
            graph[v].append((u, w))

        dist = [float('inf')] * n
        dist[0] = 0
        heap = [(0, 0)]

        while heap:
            curr_dist, node = popHeap(heap)
            if curr_dist > dist[node]:
                continue
            for nei, wght in graph[node]:
                ndist = curr_dist + wght
                if ndist < dist[nei]:
                    dist[nei] = ndist
                    insertHeap(heap, (ndist, nei))

        visited = [False] * n
        edges_on_paths = set()
        stack = [(n - 1, dist[n - 1])]

        while stack:
            curr_node, curr_dist = stack.pop()
            if visited[curr_node]:
                continue
            visited[curr_node] = True
            for nei, wght in graph[curr_node]:
                if curr_dist == dist[nei] + wght:
                    lower = curr_node if curr_node < nei else nei
                    higher = curr_node if curr_node > nei else nei
                    edges_on_paths.add((lower, higher))
                    stack.append((nei, dist[nei]))

        result = []
        for u, v, _ in edges:
            low = u if u < v else v
            high = u if u > v else v
            result.append((low, high) in edges_on_paths)

        return result