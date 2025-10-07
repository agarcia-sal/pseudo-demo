class Solution:
    def countGoodIntegers(self, j: int, m: int) -> int:
        def computeFactorial(num: int) -> int:
            if num <= 1:
                return 1
            else:
                return num * computeFactorial(num - 1)

        def buildFactorials(limit: int, resultList: list) -> None:
            pivot = 0
            while pivot <= limit:
                resultList.append(computeFactorial(pivot))
                pivot += 1

        def incrementMapCount(key: str, map_obj: dict) -> None:
            if key not in map_obj:
                map_obj[key] = 1
            else:
                map_obj[key] += 1

        def sortCharsAscending(text: str) -> str:
            charArray = list(text)
            quickSort(charArray, 0, len(charArray) - 1)
            return ''.join(charArray)

        def quickSort(arr: list, low: int, high: int) -> None:
            if low < high:
                pIndex = partition(arr, low, high)
                quickSort(arr, low, pIndex - 1)
                quickSort(arr, pIndex + 1, high)

        def partition(arr: list, lo: int, hi: int) -> int:
            pivotVal = arr[hi]
            idx = lo - 1
            k = lo
            while k <= hi - 1:
                if arr[k] <= pivotVal:
                    idx += 1
                    arr[idx], arr[k] = arr[k], arr[idx]
                k += 1
            arr[idx + 1], arr[hi] = arr[hi], arr[idx + 1]
            return idx + 1

        def reverseString(st: str) -> str:
            arr = list(st)
            left = 0
            right = len(arr) - 1
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
            return ''.join(arr)

        def substringFromIndex(src: str, startIdx: int) -> str:
            lengthSrc = len(src)
            result = ''
            pos = startIdx
            while pos < lengthSrc:
                result += src[pos]
                pos += 1
            return result

        def intToString(value: int) -> str:
            if value == 0:
                return "0"
            digits = []
            number = value
            while number > 0:
                digitVal = number % 10
                digitsAppend(digits, charFromDigit(digitVal))
                number //= 10
            reverseListInPlace(digits)
            return ''.join(digits)

        def reverseListInPlace(lst: list) -> None:
            leftIdx = 0
            rightIdx = len(lst) - 1
            while leftIdx < rightIdx:
                lst[leftIdx], lst[rightIdx] = lst[rightIdx], lst[leftIdx]
                leftIdx += 1
                rightIdx -= 1

        def digitsAppend(lst: list, ch: str) -> None:
            lst.append(ch)

        def charFromDigit(d: int) -> str:
            return chr(d + ord('0'))

        def addToSetIfAbsent(element: str, setCollection: set) -> None:
            if element not in setCollection:
                setCollection.add(element)

        def mapCharFrequencies(text: str) -> dict:
            freqMap = dict()
            idxPos = 0
            while idxPos < len(text):
                incrementMapCount(text[idxPos], freqMap)
                idxPos += 1
            return freqMap

        def isDivisible(numStr: str, divisor: int) -> bool:
            # convert numStr to int safely
            return int(numStr) % divisor == 0

        def combineStrings(front: str, back: str) -> str:
            return front + back

        def sliceStringReversedSegment(text: str, start: int) -> str:
            return substringFromIndex(reverseString(text), start)

        # Initialize
        p = 0
        factorialList = []
        buildFactorials(j, factorialList)

        totalSum = 0
        coverageSet = set()

        baseNumber = 10 ** ((j - 1) // 2)
        upperBound = baseNumber * 10 - 1

        # Process candidate number v in [baseNumber, upperBound]
        def processCandidate(num: int) -> None:
            nonlocal totalSum

            strNum = intToString(num)
            suffix = sliceStringReversedSegment(strNum, j % 2)
            fullStr = combineStrings(strNum, suffix)

            if not isDivisible(fullStr, m):
                return

            sortedStr = sortCharsAscending(fullStr)
            if sortedStr in coverageSet:
                return
            coverageSet.add(sortedStr)

            frequencyMap = mapCharFrequencies(sortedStr)

            if '0' in frequencyMap and frequencyMap['0'] > 0:
                # (j - freq('0')) * factorialList[j - 1] // product of factorials of frequencies
                numerator = (j - frequencyMap['0']) * factorialList[j - 1]
            else:
                numerator = factorialList[j]

            denominator = 1
            for val in frequencyMap.values():
                denominator *= factorialList[val]

            resVal = numerator // denominator

            totalSum += resVal

        def iterateCandidates() -> None:
            v = baseNumber
            while v <= upperBound:
                processCandidate(v)
                v += 1

        iterateCandidates()

        return totalSum