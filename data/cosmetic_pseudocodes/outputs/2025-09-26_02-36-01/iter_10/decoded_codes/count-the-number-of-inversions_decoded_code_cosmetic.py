class Solution:
    def numberOfPermutations(self, n, requirements):
        MODULO = 10**9 + 7

        requirementsMap = {}
        for req in requirements:
            requirementsMap[req[0]] = req[1]

        def count_permutations(prefixLen, inversionCount, usedMask):
            def getRequirement(key):
                return requirementsMap.get(key, inversionCount)

            if prefixLen == n:
                if inversionCount == requirementsMap.get(n, 0) - 1:
                    return 1
                else:
                    return 0

            if prefixLen > 0:
                targetValue = inversionCount
                if n in requirementsMap:
                    targetValue = requirementsMap.get(prefixLen, inversionCount) - 1 if prefixLen in requirementsMap else inversionCount
                    if inversionCount != targetValue:
                        return 0

            totalCount = 0

            def singleIterFunc(currentNumber):
                nonlocal totalCount
                if (usedMask & (1 << currentNumber)) == 0:
                    inversionAcc = inversionCount
                    innerCounter = currentNumber + 1
                    while innerCounter <= n - 1:
                        if (usedMask & (1 << innerCounter)) != 0:
                            inversionAcc += 1
                        innerCounter += 1
                    totalCount = (totalCount + count_permutations(prefixLen + 1, inversionAcc, usedMask | (1 << currentNumber))) % MODULO

            counter = 0
            while counter <= n - 1:
                singleIterFunc(counter)
                counter += 1

            return totalCount

        return count_permutations(0, 0, 0)