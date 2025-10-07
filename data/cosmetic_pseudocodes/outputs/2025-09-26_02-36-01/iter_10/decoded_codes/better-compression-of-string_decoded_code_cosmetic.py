class Solution:
    def betterCompression(self, compressed: str) -> str:
        def isAlpha(ch: str) -> bool:
            return ('A' <= ch <= 'Z') or ('a' <= ch <= 'z')

        def toInt(ch: str) -> int:
            return ord(ch) - ord('0')

        def dictGetOrZero(d: dict, key):
            return d[key] if key in d else 0

        def dictKeys(d: dict) -> list:
            keysList = []
            for k in d:
                keysList.append(k)
            return keysList

        def listSortAlpha(arr: list) -> list:
            # Simple selection sort
            n = len(arr)
            for i in range(n - 1):
                for j in range(i + 1, n):
                    if arr[j] < arr[i]:
                        arr[i], arr[j] = arr[j], arr[i]
            return arr

        def intToStr(n: int) -> str:
            if n == 0:
                return "0"

            digitsArr = []

            def helper(x: int):
                if x == 0:
                    return
                helper(x // 10)
                digitsArr.append(chr((x % 10) + ord('0')))

            helper(n)
            res = ""
            for c in digitsArr:
                res += c
            return res

        def strConcat(strList: list) -> str:
            result = ""
            for elem in strList:
                result += elem
            return result

        def appendToList(lst: list, val):
            lst_len = len(lst)
            if lst_len == 0:
                lst.append(val)
            else:
                # lst[length(lst)] = val  in pseudocode means append at end
                lst.append(val)

        def forCharsRec(index: int, charsList: list, fn):
            if index >= len(charsList):
                return
            fn(charsList[index])
            forCharsRec(index + 1, charsList, fn)

        dc = {}
        cc = ""
        ccount = 0

        def processChar(ch: str):
            nonlocal cc, ccount
            if isAlpha(ch):
                if cc != "":
                    dc[cc] = dictGetOrZero(dc, cc) + ccount
                cc = ch
                ccount = 0
            else:
                ccount = ccount * 10 + toInt(ch)

        # Use list of characters for better compatibility with pseudocode style
        forCharsRec(0, list(compressed), processChar)

        if cc != "":
            dc[cc] = dictGetOrZero(dc, cc) + ccount

        keysArr = dictKeys(dc)
        sortedKeys = listSortAlpha(keysArr)

        parts = []

        def buildPart(ch: str):
            appendToList(parts, ch + intToStr(dc[ch]))

        forCharsRec(0, sortedKeys, buildPart)

        better_compressed = strConcat(parts)
        return better_compressed