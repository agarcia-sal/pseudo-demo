class Solution:
    def maxTotalReward(self, rewardValues):
        def localSort(lst):
            def insertSorted(elem, sortedList):
                if not sortedList:
                    return [elem]
                elif elem < sortedList[0]:
                    return [elem] + sortedList
                else:
                    return [sortedList[0]] + insertSorted(elem, sortedList[1:])

            def sorter(unsorted, sortedAcc):
                if not unsorted:
                    return sortedAcc
                else:
                    return sorter(unsorted[1:], insertSorted(unsorted[0], sortedAcc))

            return sorter(lst, [])

        alpha = localSort(rewardValues)
        beta = 1

        def computeBeta(lst, acc):
            if not lst:
                return acc
            else:
                x = lst[0]
                mask1 = 1 << x
                mask2 = ((acc & (mask1 - 1)) << x)
                newAcc = acc | mask2
                return computeBeta(lst[1:], newAcc)

        beta = computeBeta(alpha, beta)
        gamma = 0

        while (1 << gamma) <= beta:
            gamma += 1

        return gamma - 1