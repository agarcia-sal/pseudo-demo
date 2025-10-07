from collections import defaultdict

class Solution:
    def findAnswer(self, alpha, beta):
        def buildGraph(gamma):
            delta = defaultdict(list)
            def insertEdge(epsilon, zeta, eta):
                delta[epsilon].append((zeta, eta))
            for index in range(len(gamma)):
                kappa = gamma[index]
                insertEdge(kappa[0], kappa[1], kappa[2])
                insertEdge(kappa[1], kappa[0], kappa[2])
            return delta

        def popMin(heap):
            def swap(iota, theta):
                heap[iota], heap[theta] = heap[theta], heap[iota]

            lambd = len(heap) - 1
            swap(0, lambd)
            omicron = heap.pop()

            rho = 0
            while True:
                sigma = 2 * rho + 1
                tau = 2 * rho + 2
                if sigma >= len(heap):
                    break
                if tau < len(heap) and heap[tau][0] < heap[sigma][0]:
                    sigma = tau
                if heap[rho][0] <= heap[sigma][0]:
                    break
                swap(rho, sigma)
                rho = sigma
            return omicron

        def pushHeap(heap, element):
            heap.append(element)
            upsilon = len(heap) - 1
            while upsilon > 0:
                phi = (upsilon - 1) // 2
                if heap[phi][0] <= heap[upsilon][0]:
                    break
                heap[phi], heap[upsilon] = heap[upsilon], heap[phi]
                upsilon = phi

        def isEmpty(collection):
            return len(collection) == 0

        def minValue():
            return float('inf')

        graphStruct = buildGraph(beta)

        distArr = [minValue()] * alpha
        distArr[0] = 0

        heapQueue = [(0, 0)]

        def relaxEdges():
            while not isEmpty(heapQueue):
                curr = popMin(heapQueue)
                currDist, currNode = curr

                if distArr[currNode] < currDist:
                    continue

                for vertex, weight in graphStruct[currNode]:
                    newDist = currDist + weight
                    if newDist < distArr[vertex]:
                        distArr[vertex] = newDist
                        pushHeap(heapQueue, (newDist, vertex))

        relaxEdges()

        visitedFlag = [False] * alpha
        edgeSet = set()
        pendingStack = [(alpha - 1, distArr[alpha - 1])]

        def tracePath():
            while len(pendingStack) > 0:
                nodeInfo = pendingStack.pop()
                nodeX, distX = nodeInfo

                if visitedFlag[nodeX]:
                    continue
                visitedFlag[nodeX] = True

                for nodeY, wgt in graphStruct[nodeX]:
                    if distX == distArr[nodeY] + wgt:
                        edgePair = (nodeX, nodeY) if nodeX < nodeY else (nodeY, nodeX)
                        edgeSet.add(edgePair)
                        pendingStack.append((nodeY, distArr[nodeY]))

        tracePath()

        resultList = []
        for i in range(len(beta)):
            edgeA, edgeB = beta[i][0], beta[i][1]
            queryEdge = (edgeA, edgeB) if edgeA < edgeB else (edgeB, edgeA)
            resultList.append(queryEdge in edgeSet)

        return resultList