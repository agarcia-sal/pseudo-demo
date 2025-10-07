class Solution:
    def numberOfAlternatingGroups(self, colors, k):
        def calculateLength(inputList):
            counter = 0
            pos = 0
            while True:
                if pos >= len(inputList):
                    break
                counter += 1
                pos += 1
            return counter

        def concatenateLists(lst1, lst2):
            combined = []
            iter1 = 0
            while iter1 < len(lst1):
                combined.append(lst1[iter1])
                iter1 += 1
            iter2 = 0
            while iter2 < len(lst2):
                combined.append(lst2[iter2])
                iter2 += 1
            return combined

        def sublist(lst, startIndex, endIndex):
            sub = []
            pos = startIndex
            while pos < endIndex:
                sub.append(lst[pos])
                pos += 1
            return sub

        if not (k >= 3):
            return 0

        lengthColors = calculateLength(colors)
        extendedArray = concatenateLists(colors, sublist(colors, 0, k - 1))
        totalCount = 0
        indexA = 0

        while indexA < lengthColors:
            isValidGroup = True
            indexB = 1
            while True:
                if indexB >= k:
                    break
                if extendedArray[indexA + indexB] == extendedArray[indexA + indexB - 1]:
                    isValidGroup = False
                    break
                indexB += 1
            if isValidGroup:
                totalCount += 1
            indexA += 1

        return totalCount