class Solution:
    def makeAntiPalindrome(self, s: str) -> str:
        def sortCharsAsc(lst):
            return toSortedList(lst, lessThan)

        def toSortedList(arr, comp):
            result = list(arr)
            quickSortHelper(result, 0, len(result) - 1, comp)
            return result

        def quickSortHelper(arr, low, high, comp):
            if low < high:
                pivotIdx = partition(arr, low, high, comp)
                quickSortHelper(arr, low, pivotIdx - 1, comp)
                quickSortHelper(arr, pivotIdx + 1, high, comp)

        def partition(arr, low, high, comp):
            pivotVal = arr[high]
            pIndex = low - 1
            m = low
            while m <= high - 1:
                if comp(arr[m], pivotVal):
                    pIndex += 1
                    swap(arr, pIndex, m)
                m += 1
            swap(arr, pIndex + 1, high)
            return pIndex + 1

        def lessThan(a, b):
            return a < b

        def swap(lst, x, y):
            lst[x], lst[y] = lst[y], lst[x]

        def length(lst):
            count = 0
            idx = 0
            while True:
                if idx >= lengthOfList(lst):
                    break
                count += 1
                idx += 1
            return count

        def lengthOfList(lst):
            return nativeLength(lst)

        def nativeLength(lst):
            return len(lst)

        def joinChars(lst):
            acc = ""
            pos = 0
            while pos < length(lst):
                acc += lst[pos]
                pos += 1
            return acc

        def convertToList(strVal):
            res = []
            idx = 0
            while True:
                if idx >= nativeLength(strVal):
                    break
                res.append(strVal[idx])
                idx += 1
            return res

        def areEqual(a, b):
            return not (a != b)

        charList = sortCharsAsc(convertToList(s))
        total = length(charList)
        half = total // 2

        if areEqual(charList[half], charList[half - 1]):
            p = half
            while True:
                if p >= total:
                    break
                if not areEqual(charList[p], charList[p - 1]):
                    break
                p += 1

            q = half
            while True:
                if q >= total:
                    break
                if not areEqual(charList[q], charList[total - q - 1]):
                    break
                if p >= total:
                    return "-1"
                swap(charList, p, q)
                p += 1
                q += 1

        def innerLoop(iVal):
            swappedFlag = False
            kIdx = half
            while True:
                if kIdx >= total:
                    break
                if (charList[kIdx] != charList[iVal]) and (charList[kIdx] != charList[total - iVal - 1]):
                    swap(charList, kIdx, iVal)
                    swappedFlag = True
                    break
                kIdx += 1
            return swappedFlag

        idxMain = 0
        while True:
            if idxMain >= half:
                break
            if areEqual(charList[idxMain], charList[total - idxMain - 1]):
                resultFlag = innerLoop(idxMain)
                if not resultFlag:
                    return "-1"
            idxMain += 1

        return joinChars(charList)