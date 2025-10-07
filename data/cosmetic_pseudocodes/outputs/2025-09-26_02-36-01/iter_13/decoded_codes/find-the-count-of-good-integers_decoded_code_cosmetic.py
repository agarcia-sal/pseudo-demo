class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        def computeFactorial(m: int) -> int:
            if m <= 1:
                return 1
            else:
                return m * computeFactorial(m - 1)

        def countCharacters(s: str) -> dict:
            frequency = {}

            def helper(idx: int) -> None:
                if idx >= len(s):
                    return
                ch = s[idx]
                frequency[ch] = frequency.get(ch, 0) + 1
                helper(idx + 1)

            helper(0)
            return frequency

        def sortStringChars(src: str) -> str:
            charsList = []
            idx = 0
            while idx < len(src):
                charsList.append(src[idx])
                idx += 1

            def quickSort(arr: list, low: int, high: int) -> None:
                if low < high:
                    def partition(lowP: int, highP: int) -> int:
                        pivot = arr[highP]
                        i = lowP - 1
                        j = lowP
                        while j < highP:
                            if arr[j] <= pivot:
                                i += 1
                                arr[i], arr[j] = arr[j], arr[i]
                            j += 1
                        i += 1
                        arr[i], arr[highP] = arr[highP], arr[i]
                        return i

                    p = partition(low, high)
                    quickSort(arr, low, p - 1)
                    quickSort(arr, p + 1, high)

            quickSort(charsList, 0, len(charsList) - 1)

            resStr = ""
            pos = 0
            while pos < len(charsList):
                resStr += charsList[pos]
                pos += 1
            return resStr

        def toString(num: int) -> str:
            if num == 0:
                return "0"
            digits = []
            tmp = num
            while tmp > 0:
                rem = tmp % 10
                tmp //= 10
                ch = chr(rem + 48)
                digits.append(ch)
            reversed_digits = []
            dIdx = len(digits) - 1
            while dIdx >= 0:
                reversed_digits.append(digits[dIdx])
                dIdx -= 1
            result = ""
            rIdx = 0
            while rIdx < len(reversed_digits):
                result += reversed_digits[rIdx]
                rIdx += 1
            return result

        def reverseString(s: str) -> str:
            lengthS = len(s)
            rev = ""
            idx = lengthS - 1
            while idx >= 0:
                rev += s[idx]
                idx -= 1
            return rev

        factorials = []
        index = 0
        while index < n + 1:
            factorials.append(computeFactorial(index))
            index += 1

        answer = 0
        visitedSet = set()

        baseNum = 1
        expCount = (n - 1) // 2
        expIdx = 0
        while expIdx < expCount:
            baseNum *= 10
            expIdx += 1

        current = baseNum
        limit = baseNum * 10
        while current < limit:
            s1 = toString(current)
            revS = reverseString(s1)
            addPart = ""
            startPos = n % 2
            revLen = len(revS)
            posR = startPos
            while posR < revLen:
                addPart += revS[posR]
                posR += 1
            s1 = s1 + addPart

            sInt = 0
            mul = 1
            idxS = len(s1) - 1
            while idxS >= 0:
                digit = ord(s1[idxS]) - 48
                sInt += digit * mul
                mul *= 10
                idxS -= 1

            if sInt % k != 0:
                current += 1
                continue

            t = sortStringChars(s1)

            if t in visitedSet:
                current += 1
                continue
            visitedSet.add(t)

            cnt = countCharacters(t)

            zeroChar = '0'
            zeroCount = cnt.get(zeroChar, 0)

            if zeroCount > 0:
                res = (n - zeroCount) * factorials[n - 1]
            else:
                res = factorials[n]

            for val in cnt.values():
                res //= factorials[val]

            answer += res
            current += 1

        return answer