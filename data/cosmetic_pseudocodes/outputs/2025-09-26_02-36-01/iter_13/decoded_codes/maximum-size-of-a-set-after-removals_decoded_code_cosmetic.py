class Solution:
    def maximumSetSize(self, nums1, nums2) -> int:
        alpha = len(nums1)
        beta = (0 + alpha) // 2

        distinctA = self.getDistinctItems(nums1[:], [])
        distinctB = self.getDistinctItems(nums2[:], [])

        overlap = self.findCommonElements(distinctA[:], distinctB, [])
        exclusiveA = self.removeElements(distinctA[:], overlap, [])
        exclusiveB = self.removeElements(distinctB[:], overlap, [])

        countFromA = self.minimum(beta, self.getSize(exclusiveA[:]))
        countFromB = self.minimum(beta, self.getSize(exclusiveB[:]))

        leftoverA = self.maximum(0, beta - countFromA)
        leftoverB = self.maximum(0, beta - countFromB)

        aggregateFromCommon = leftoverA + leftoverB
        contributionFromCommon = self.minimum(aggregateFromCommon, self.getSize(overlap[:]))

        overallCount = countFromA + countFromB + contributionFromCommon

        return overallCount

    def getDistinctItems(self, sourceList, resultList) -> list:
        if self.isEmpty(sourceList):
            return resultList
        else:
            item = self.removeFirst(sourceList)
            if not self.containsItem(resultList, item):
                self.appendItem(resultList, item)
            return self.getDistinctItems(sourceList, resultList)

    def findCommonElements(self, listA, listB, resultList) -> list:
        if self.isEmpty(listA):
            return resultList
        else:
            element = self.removeFirst(listA)
            if self.containsItem(listB, element):
                self.appendItem(resultList, element)
            return self.findCommonElements(listA, listB, resultList)

    def removeElements(self, source, toRemove, result) -> list:
        if self.isEmpty(source):
            return result
        else:
            element = self.removeFirst(source)
            if not self.containsItem(toRemove, element):
                self.appendItem(result, element)
            return self.removeElements(source, toRemove, result)

    def minimum(self, a: int, b: int) -> int:
        if a < b:
            return a
        return b

    def maximum(self, a: int, b: int) -> int:
        if a > b:
            return a
        return b

    def isEmpty(self, lst) -> bool:
        return self.getSize(lst) == 0

    def getSize(self, lst) -> int:
        count = 0
        # We must not modify the input list as the original pseudocode did removeFirst
        # repeatedly which mutates the list. So here we copy and remove.
        temp = lst[:]
        while not self.isEmpty(temp):
            self.removeFirst(temp)
            count += 1
        return count

    def removeFirst(self, lst) -> int:
        # We shift all elements left by one and remove the last duplicate element
        firstElement = lst[0]
        for i in range(1, self.getSize(lst)):
            lst[i-1] = lst[i]
        lst.pop()
        return firstElement

    def containsItem(self, lst, val: int) -> bool:
        idx = 0
        size = self.getSize(lst)
        while True:
            if idx >= size:
                break
            if lst[idx] == val:
                return True
            idx += 1
        return False

    def appendItem(self, lst, val: int) -> None:
        # Append val at the end of lst using index assignment as in pseudocode
        lst.append(val)