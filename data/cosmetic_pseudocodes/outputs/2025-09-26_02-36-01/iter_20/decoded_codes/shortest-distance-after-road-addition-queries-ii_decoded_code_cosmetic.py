class Solution:
    def shortestDistanceAfterQueries(self, n, queries):
        # Build adjacency list for the chain graph (0 to n-1, edges between consecutive nodes)
        graph = {i: [] for i in range(n)}
        for i in range(n - 1):
            graph[i].append((i + 1, 1))
            graph[i + 1].append((i, 1))

        def dijkstra():
            dist = [float('inf')] * n
            dist[0] = 0
            pq = [(0, 0)]  # (distance, node)

            # Custom heap pop with heapify down
            def heapPop(pq):
                def heapifyDown(arr, idx):
                    length = len(arr)
                    idx_cur = idx
                    while (left := 2 * idx_cur + 1) < length:
                        idx_swap = idx_cur
                        if arr[idx_swap][0] > arr[left][0]:
                            idx_swap = left
                        if (right := left + 1) < length and arr[idx_swap][0] > arr[right][0]:
                            idx_swap = right
                        if idx_swap == idx_cur:
                            break
                        arr[idx_cur], arr[idx_swap] = arr[idx_swap], arr[idx_cur]
                        idx_cur = idx_swap

                lastIndex = len(pq) - 1
                ret = pq[0]
                pq[0] = pq[lastIndex]
                pq.pop()
                if pq:
                    heapifyDown(pq, 0)
                return ret

            # Custom heap push with heapify up
            def heapPush(pq, elem):
                pq.append(elem)
                idx = len(pq) - 1
                while idx > 0:
                    parent = (idx - 1) // 2
                    if pq[parent][0] <= pq[idx][0]:
                        break
                    pq[parent], pq[idx] = pq[idx], pq[parent]
                    idx = parent

            active = True
            while active:
                if len(pq) < 1:
                    active = False
                    continue
                cur_dist, node = heapPop(pq)
                if cur_dist > dist[node]:
                    continue
                for neighbor, weight in graph[node]:
                    new_dist = cur_dist + weight
                    if new_dist < dist[neighbor]:
                        dist[neighbor] = new_dist
                        heapPush(pq, (new_dist, neighbor))
            return dist[n - 1]

        res = []
        for x, y in queries:
            # Add (y,1) edge from x to y; note that original adjacency is one-way in pseudocode
            graph[x].append((y, 1))
            res.append(dijkstra())

        return res