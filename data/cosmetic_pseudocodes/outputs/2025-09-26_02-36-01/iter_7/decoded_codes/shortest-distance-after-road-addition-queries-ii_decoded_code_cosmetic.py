class Solution:
    def shortestDistanceAfterQueries(self, n, queries):
        MAX_VALUE = (1 << 31) - 1

        def buildGraph(size):
            graph = {i: [] for i in range(size - 1)}
            for idx in range(size - 1):
                first = idx + 1
                second = 1
                graph[idx].append((first, second))
            if size - 1 not in graph:
                graph[size - 1] = []
            return graph

        graph = buildGraph(n)

        def dijkstra():
            distances = [MAX_VALUE] * n
            distances[0] = 0
            priorityQueue = [(0, 0)]

            def popLowest():
                min_index = 0
                for i in range(1, len(priorityQueue)):
                    if priorityQueue[i][0] < priorityQueue[min_index][0]:
                        min_index = i
                return priorityQueue.pop(min_index)

            while priorityQueue:
                currDistance, currNode = popLowest()
                if currDistance > distances[currNode]:
                    continue
                for adjNode, weight in graph[currNode]:
                    totalDist = currDistance + weight
                    if totalDist < distances[adjNode]:
                        distances[adjNode] = totalDist
                        priorityQueue.append((totalDist, adjNode))
            return distances[n - 1]

        output = []
        ind = 0
        while ind < len(queries):
            x, y = queries[ind]
            if x not in graph:
                graph[x] = []
            graph[x].append((y, 1))
            output.append(dijkstra())
            ind += 1

        return output