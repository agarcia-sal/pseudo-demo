class Solution:
    def shortestDistanceAfterQueries(self, n, queries):
        graph = {x: [] for x in range(n)}

        def populateEdges(k):
            if k > n - 2:
                return
            nxt = k + 1
            graph[k].append((nxt, 1))
            populateEdges(k + 1)

        populateEdges(0)

        def dijkstra():
            dist = [float('inf')] * n
            dist[0] = 0

            pq = [(0, 0)]

            def siftDownHeap():
                if not pq:
                    return
                smallest_idx = 0

                def leftChild(i): return 2 * i + 1
                def rightChild(i): return 2 * i + 2

                while True:
                    lc = leftChild(smallest_idx)
                    rc = rightChild(smallest_idx)
                    min_idx = smallest_idx

                    if lc < len(pq) and pq[lc][0] < pq[min_idx][0]:
                        min_idx = lc
                    if rc < len(pq) and pq[rc][0] < pq[min_idx][0]:
                        min_idx = rc
                    if min_idx == smallest_idx:
                        break
                    pq[smallest_idx], pq[min_idx] = pq[min_idx], pq[smallest_idx]
                    smallest_idx = min_idx

            def heapPush(elem):
                pq.append(elem)
                idx = len(pq) - 1
                while idx > 0:
                    parent = (idx - 1) // 2
                    if pq[parent][0] > pq[idx][0]:
                        pq[parent], pq[idx] = pq[idx], pq[parent]
                        idx = parent
                    else:
                        break

            def heapPop():
                if not pq:
                    return None
                topElem = pq[0]
                pq[0] = pq[-1]
                pq.pop()
                siftDownHeap()
                return topElem

            def processQueue():
                t = heapPop()
                if t is None:
                    return None
                return t

            def visitNeighbors(currDist, currNode):
                for (nbr, wgt) in graph[currNode]:
                    tentative = currDist + wgt
                    if tentative < dist[nbr]:
                        dist[nbr] = tentative
                        heapPush((tentative, nbr))

            while True:
                popped = processQueue()
                if popped is None:
                    break
                currDist, currNode = popped
                if currDist > dist[currNode]:
                    continue
                visitNeighbors(currDist, currNode)

            return dist[n - 1]

        accum = []

        def processQueries(ix):
            if ix >= len(queries):
                return
            a, b = queries[ix]
            graph[a].append((b, 1))
            dRes = dijkstra()
            accum.append(dRes)
            processQueries(ix + 1)

        processQueries(0)

        return accum