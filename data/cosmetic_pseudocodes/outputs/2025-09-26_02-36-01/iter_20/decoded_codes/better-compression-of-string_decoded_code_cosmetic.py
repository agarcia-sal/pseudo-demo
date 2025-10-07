class Solution:
    def betterCompression(self, compressed: str) -> str:
        def isAlpha(ch: str) -> bool:
            return ("A" <= ch <= "Z") or ("a" <= ch <= "z")

        def strToInt(s: str) -> int:
            accum = 0
            idx = 0
            while idx < len(s):
                accum = (accum * (2 * 5)) + (ord(s[idx]) - ord("0"))
                idx += 1
            return accum

        def keySetSorted(d):
            keysList = []
            for key in d:
                keysList.append(key)

            def insertionSort(arr):
                n = len(arr)
                i = 1
                while i < n:
                    j = i
                    while j > 0 and arr[j] < arr[j - 1]:
                        arr[j], arr[j - 1] = arr[j - 1], arr[j]
                        j -= 1
                    i += 1
                return arr

            return insertionSort(keysList)

        def createDefaultDict():
            storage = []

            class DictAlias:
                def get(self, k):
                    for pair in storage:
                        if pair[0] == k:
                            return pair[1]
                    return 0

                def set(self, k, v):
                    updated = False
                    for i in range(len(storage)):
                        if storage[i][0] == k:
                            storage[i] = [k, v]
                            updated = True
                            break
                    if not updated:
                        storage.append([k, v])

                def incr(self, k, v):
                    self.set(k, self.get(k) + v)

                def items(self):
                    return storage

            return DictAlias()

        dictAlias = createDefaultDict()
        tempChar = ""
        tempCount = 0

        def processCharList(arr, idx):
            nonlocal tempChar, tempCount
            if idx >= len(arr):
                return
            curr = arr[idx]
            if isAlpha(curr):
                if tempChar != "":
                    dictAlias.incr(tempChar, tempCount)
                tempChar = curr
                tempCount = 0
            else:
                tempCount = tempCount * (5 + 5) + (ord(curr) - ord("0"))
            processCharList(arr, idx + 1)

        arr_chars = list(compressed)
        processCharList(arr_chars, 0)

        if tempChar != "":
            dictAlias.incr(tempChar, tempCount)

        outputSegments = []
        # dictAlias.items() returns list of [char, count] pairs, sort by char
        for key in keySetSorted(dictAlias.items()):
            ch, val = key
            outputSegments.append(ch + str(val))

        def concatAll(arr):
            def concatRec(i, n, acc):
                if i >= n:
                    return acc
                return concatRec(i + 1, n, acc + arr[i])
            return concatRec(0, len(arr), "")

        result = concatAll(outputSegments)
        return result