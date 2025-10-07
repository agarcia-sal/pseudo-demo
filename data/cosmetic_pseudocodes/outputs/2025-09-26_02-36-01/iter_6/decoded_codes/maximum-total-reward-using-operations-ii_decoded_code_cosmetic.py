class Solution:
    def maxTotalReward(self, rewardValues):
        def computeBitLength(x):
            count = 0
            while x > 0:
                count += 1
                x >>= 1
            return count

        def sortList(lst):
            if len(lst) <= 1:
                return lst
            pivotIndex = (len(lst) - 1) // 2
            pivotValue = lst[pivotIndex]
            leftPartition = []
            rightPartition = []
            idx = 0
            while True:
                if idx >= len(lst):
                    break
                if idx != pivotIndex:
                    if lst[idx] < pivotValue:
                        leftPartition.append(lst[idx])
                    else:
                        rightPartition.append(lst[idx])
                idx += 1
            return sortList(leftPartition) + [pivotValue] + sortList(rightPartition)

        def uniqueList(lst):
            seen = set()
            result = []
            def helper(i):
                if i >= len(lst):
                    return
                element = lst[i]
                if element not in seen:
                    seen.add(element)
                    result.append(element)
                helper(i + 1)
            helper(0)
            return result

        sortedUnique = uniqueList(sortList(rewardValues))
        flag = 1
        def iterateElements(i, acc):
            if i >= len(sortedUnique):
                return acc
            val = sortedUnique[i]
            shiftedPart = ((1 << val) - 1) << val
            newAcc = acc | (acc & shiftedPart)
            return iterateElements(i + 1, newAcc)

        flag = iterateElements(0, flag)
        return computeBitLength(flag) - 1