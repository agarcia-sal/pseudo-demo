class Solution:
    def maxTotalReward(self, rewardValues):
        def bitShiftLeft(base, exp):
            if exp == 0:
                return 1
            else:
                return 2 * bitShiftLeft(base, exp - 1)

        def bitCount(num):
            counter = 0
            tempNum = num
            while tempNum > 0:
                flag = tempNum & 1
                counter += flag
                tempNum //= 2
            return counter

        def insertSortedSet(collection, element):
            if not collection:
                collection.append(element)
                return
            i = 0
            while i < len(collection) and collection[i] < element:
                i += 1
            if i == len(collection) or collection[i] != element:
                collection.insert(i, element)

        uniqueSorted = []
        idx = 0
        while idx < len(rewardValues):
            insertSortedSet(uniqueSorted, rewardValues[idx])
            idx += 1

        accumulated = 1
        j = 0
        while j < len(uniqueSorted):
            shiftedOne = bitShiftLeft(2, uniqueSorted[j])
            mask = shiftedOne - 1
            bitwiseOp = accumulated & mask
            accumulated = accumulated | (bitwiseOp << uniqueSorted[j])
            j += 1

        def bitLength(value):
            lengthCount = 0
            valCopy = value
            while valCopy > 0:
                valCopy //= 2
                lengthCount += 1
            return lengthCount

        resultLength = bitLength(accumulated) - 1
        return resultLength