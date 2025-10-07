class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        def factorialCalc(u: int) -> int:
            if u <= 1:
                return 1
            else:
                return u * factorialCalc(u - 1)

        def countCharacters(s: str) -> dict[str, int]:
            def helperCount(chars: list[str], idx: int, acc: dict[str, int]) -> dict[str, int]:
                if idx > len(chars) - 1:
                    return acc
                currChar = chars[idx]
                acc[currChar] = acc.get(currChar, 0) + 1
                return helperCount(chars, idx + 1, acc)

            return helperCount(list(s), 0, {})

        def sortString(input_str: str) -> str:
            def insertChar(sortedList: list[str], ch: str) -> list[str]:
                if not sortedList:
                    return [ch]
                elif ch <= sortedList[0]:
                    return [ch] + sortedList
                else:
                    return [sortedList[0]] + insertChar(sortedList[1:], ch)

            def sortHelper(chars: list[str]) -> list[str]:
                if len(chars) == 0:
                    return []
                else:
                    return insertChar(sortHelper(chars[1:]), chars[0])

            return ''.join(sortHelper(list(input_str)))

        def reverseString(input_str: str) -> str:
            def revHelper(chars: list[str], idx: int, acc: list[str]) -> list[str]:
                if idx < 0:
                    return acc
                else:
                    return revHelper(chars, idx - 1, acc + [chars[idx]])

            return ''.join(revHelper(list(input_str), len(input_str) - 1, []))

        def stringToInt(s: str) -> int:
            def toIntHelper(chars: list[str], idx: int, acc: int) -> int:
                if idx > len(chars) - 1:
                    return acc
                digitValue = ord(chars[idx]) - ord('0')
                return toIntHelper(chars, idx + 1, acc * 10 + digitValue)

            return toIntHelper(list(s), 0, 0)

        def intToString(num: int) -> str:
            if num == 0:
                return "0"

            def intToStrRecur(x: int, acc: list[str]) -> list[str]:
                if x == 0:
                    return acc
                remainder = x % 10
                charDigit = chr(remainder + ord('0'))
                return intToStrRecur(x // 10, [charDigit] + acc)

            return ''.join(intToStrRecur(num, []))

        def pow(baseVal: int, exp: int) -> int:
            if exp == 0:
                return 1
            else:
                return baseVal * pow(baseVal, exp - 1)

        def substringFrom(s: str, startIdx: int) -> str:
            def substrHelper(chars: list[str], idx: int, acc: list[str]) -> list[str]:
                if idx > len(chars) - 1:
                    return acc
                else:
                    return substrHelper(chars, idx + 1, acc + [chars[idx]])

            return ''.join(substrHelper(list(s), startIdx, []))

        def concatStrings(a: str, b: str) -> str:
            return a + b

        def appendToList(lst: list[int], val: int) -> list[int]:
            return lst + [val]

        def contains(s: set[str], elem: str) -> bool:
            return elem in s

        def addToSet(s: set[str], elem: str) -> set[str]:
            s2 = set(s)
            s2.add(elem)
            return s2

        def getSetValuesCount(m: dict[str, int]) -> list[int]:
            def valHelper(keys: list[str], idx: int, acc: list[int]) -> list[int]:
                if idx > len(keys) - 1:
                    return acc
                return valHelper(keys, idx + 1, acc + [m[keys[idx]]])

            return valHelper(list(m.keys()), 0, [])

        def mapContainsKey(m: dict[str, int], key: str) -> bool:
            return key in m

        def mapGet(m: dict[str, int], key: str) -> int:
            return m[key]

        def integerDiv(a: int, b: int) -> int:
            return a // b

        def integerMod(a: int, b: int) -> int:
            return a - (integerDiv(a, b) * b)

        def factorialListCreate(limit: int) -> list[int]:
            def facHelper(x: int, acc: list[int]) -> list[int]:
                if x > limit - 1:
                    return acc
                return facHelper(x + 1, appendToList(acc, factorialCalc(x)))

            return facHelper(0, [])

        micv = factorialListCreate(n + 1)
        lrah = 0
        zoin = set()
        rexv = pow(10, integerDiv(n - 1, 2))

        def processIteration(mn: int, mx: int, answer: int, visited: set[str]) -> int:
            if mn > mx:
                return answer
            stfx = intToString(mn)
            revStfx = reverseString(stfx)
            substrRevStfx = substringFrom(revStfx, integerMod(n, 2))
            combinedStr = concatStrings(stfx, substrRevStfx)
            if integerMod(stringToInt(combinedStr), k) != 0:
                return processIteration(mn + 1, mx, answer, visited)
            sortedStr = sortString(combinedStr)
            if contains(visited, sortedStr):
                return processIteration(mn + 1, mx, answer, visited)
            newVisited = addToSet(visited, sortedStr)
            counts = countCharacters(sortedStr)
            if mapContainsKey(counts, '0') and mapGet(counts, '0') > 0:
                partRes = (n - mapGet(counts, '0')) * micv[n - 1]
            else:
                partRes = micv[n]

            def divideByFactorials(val: int, vals: list[int], idx: int) -> int:
                if idx > len(vals) - 1:
                    return val
                return divideByFactorials(integerDiv(val, micv[vals[idx]]), vals, idx + 1)

            resVal = divideByFactorials(partRes, getSetValuesCount(counts), 0)
            return processIteration(mn + 1, mx, answer + resVal, newVisited)

        return processIteration(rexv, (rexv * 10) - 1, lrah, zoin)