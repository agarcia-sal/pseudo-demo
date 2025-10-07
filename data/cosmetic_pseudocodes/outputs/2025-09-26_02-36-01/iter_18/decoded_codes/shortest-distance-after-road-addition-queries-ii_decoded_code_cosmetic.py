class Solution:
    def shortestDistanceAfterQueries(self, n, queries):
        adjacency = {x: [] for x in range(n)}
        idx = 0
        while idx <= n - 2:
            adjacency[idx].append((idx + 1, 1))
            idx += 1

        def dijkstra():
            distances = [float('inf')] * n
            distances[0] = 0
            heap = [(0, 0)]

            def siftDown(heapList):
                root = 0
                endIndex = len(heapList) - 1
                while True:
                    child = 2 * root + 1
                    if child > endIndex:
                        break
                    swap = root
                    if heapList[swap][0] > heapList[child][0]:
                        swap = child
                    if child + 1 <= endIndex and heapList[swap][0] > heapList[child + 1][0]:
                        swap = child + 1
                    if swap == root:
                        break
                    heapList[root], heapList[swap] = heapList[swap], heapList[root]
                    root = swap

            def siftUp(heapList):
                idx = len(heapList) - 1
                while idx > 0:
                    parent = (idx - 1) >> 1
                    if heapList[parent][0] <= heapList[idx][0]:
                        break
                    heapList[idx], heapList[parent] = heapList[parent], heapList[idx]
                    idx = parent

            def heappush(heapList, element):
                heapList.append(element)
                siftUp(heapList)

            def heappop(heapList):
                lastElement = heapList.pop()
                if not heapList:
                    return lastElement
                minItem = heapList[0]
                heapList[0] = lastElement
                siftDown(heapList)
                return minItem

            def isEmpty(collection):
                return len(collection) == 0

            while not isEmpty(heap):
                currDistance, currVertex = heappop(heap)
                if currDistance > distances[currVertex]:
                    continue
                for dest, w in adjacency[currVertex]:
                    tentativeDist = currDistance + w
                    if tentativeDist < distances[dest]:
                        distances[dest] = tentativeDist
                        heappush(heap, (tentativeDist, dest))
            return distances[n - 1]

        outputList = []
        for firstNode, secondNode in queries:
            adjacency[firstNode].append((secondNode, 1))
            outputList.append(dijkstra())

        return outputList