class Solution:
    def mostFrequentIDs(self, nums, freq):
        def getCount(dct, ky):
            return dct[ky] if ky in dct else 0

        histo = {}
        heapContainer = []
        outputList = []

        def pushHeap(hp, val):
            hp.append(val)
            pos = len(hp) - 1
            while pos > 0:
                p = (pos - 1) // 2
                if hp[p][0] <= hp[pos][0]:
                    break
                hp[p], hp[pos] = hp[pos], hp[p]
                pos = p

        def popHeap(hp):
            res = hp[0]
            last = hp.pop()
            if hp:
                hp[0] = last
                pos = 0
                while True:
                    l = 2 * pos + 1
                    r = 2 * pos + 2
                    smallest = pos
                    if l < len(hp) and hp[l][0] < hp[smallest][0]:
                        smallest = l
                    if r < len(hp) and hp[r][0] < hp[smallest][0]:
                        smallest = r
                    if smallest == pos:
                        break
                    hp[pos], hp[smallest] = hp[smallest], hp[pos]
                    pos = smallest
            return res

        def isEmpty(hp):
            return len(hp) == 0

        def topHeap(hp):
            return hp[0]

        def lenList(lst):
            return len(lst)

        def appendList(lst, val):
            lst.append(val)

        def incrementDictDict(dct, ky, v):
            if ky in dct:
                dct[ky] += v
            else:
                dct[ky] = v

        def elementAt(lst, index):
            return lst[index]

        def pairFirst(p):
            return p[0]

        def pairSecond(p):
            return p[1]

        def negative(x):
            return -x

        def tuplesMake(a, b):
            return [a, b]

        def correspondingIter(listA, listB, fn, idx):
            if idx >= lenList(listA):
                return
            fn(elementAt(listA, idx), elementAt(listB, idx))
            correspondingIter(listA, listB, fn, idx + 1)

        def loopBody(nm, fq):
            incrementDictDict(histo, nm, fq)
            pushHeap(heapContainer, tuplesMake(negative(histo[nm]), nm))
            while (not isEmpty(heapContainer) and 
                   negative(pairFirst(topHeap(heapContainer))) != histo[pairSecond(topHeap(heapContainer))]):
                popHeap(heapContainer)
            if not isEmpty(heapContainer):
                appendList(outputList, negative(pairFirst(topHeap(heapContainer))))
            else:
                appendList(outputList, 0)

        correspondingIter(nums, freq, loopBody, 0)
        return outputList