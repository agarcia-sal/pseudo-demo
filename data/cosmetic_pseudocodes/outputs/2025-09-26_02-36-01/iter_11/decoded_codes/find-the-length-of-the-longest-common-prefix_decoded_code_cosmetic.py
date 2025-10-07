class Solution:
    def longestCommonPrefix(self, arr1, arr2):
        def stringFromNumber(x):
            result = ""
            temp = x
            while True:
                digit = temp % 10
                temp = (temp - digit) // 10
                result = chr(48 + digit) + result
                if temp == 0:
                    break
            return result

        setA = set()
        setB = set()

        idxA = 0
        while idxA < len(arr1):
            conv = stringFromNumber(arr1[idxA])
            posA = 1
            while posA <= len(conv):
                setA.add(conv[:posA])
                posA += 1
            idxA += 1

        idxB = 0
        while idxB < len(arr2):
            convB = stringFromNumber(arr2[idxB])
            posB = 1
            while posB <= len(convB):
                setB.add(convB[:posB])
                posB += 1
            idxB += 1

        maxPrefixLength = 0

        def checkPrefix(pfx):
            nonlocal maxPrefixLength
            if pfx in setB:
                lenP = len(pfx)
                if lenP > maxPrefixLength:
                    maxPrefixLength = lenP

        arrPrefixes = list(setA)

        def iteratePrefixes(i):
            if i >= len(arrPrefixes):
                return
            checkPrefix(arrPrefixes[i])
            iteratePrefixes(i + 1)

        iteratePrefixes(0)

        return maxPrefixLength