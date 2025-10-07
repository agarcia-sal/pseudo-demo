class Solution:
    def mostFrequentIDs(self, numbers, frequencies):
        def addToDictionary(d, key, value):
            if key in d:
                d[key] += value
            else:
                d[key] = value

        def heapPush(heap, element):
            heap.append(element)
            index = len(heap) - 1
            while index > 0:
                parent = (index - 1) // 2
                if heap[parent][0] >= heap[index][0]:
                    break
                heap[parent], heap[index] = heap[index], heap[parent]
                index = parent

        def heapPop(heap):
            if len(heap) == 0:
                return None
            result = heap[0]
            heap[0] = heap[-1]
            heap.pop()
            index = 0
            length = len(heap)
            while True:
                left = index * 2 + 1
                right = index * 2 + 2
                largest = index

                if left < length and heap[left][0] > heap[largest][0]:
                    largest = left
                if right < length and heap[right][0] > heap[largest][0]:
                    largest = right

                if largest == index:
                    break

                heap[index], heap[largest] = heap[largest], heap[index]
                index = largest
            return result

        def heapPeek(heap):
            if len(heap) > 0:
                return heap[0]
            return None

        frequencyMap = {}
        heapList = []
        outputList = []

        def processPair(index, nList, fList):
            if index >= len(nList):
                return
            addToDictionary(frequencyMap, nList[index], fList[index])
            heapPush(heapList, (-frequencyMap[nList[index]], nList[index]))

            while len(heapList) > 0:
                topPair = heapPeek(heapList)
                freqValueMatch = frequencyMap[topPair[1]]
                if -topPair[0] == freqValueMatch:
                    break
                heapPop(heapList)

            if len(heapList) > 0:
                outputList.append(-heapPeek(heapList)[0])
            else:
                outputList.append(0)

            processPair(index + 1, nList, fList)

        processPair(0, numbers, frequencies)
        return outputList