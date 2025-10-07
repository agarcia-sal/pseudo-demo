class Solution:
    def compressedString(self, word: str) -> str:
        def toStr(num: int) -> str:
            resStr = ""
            rem = num
            while True:
                if rem == 0:
                    break
                resStr = chr((rem % 10) + 48) + resStr
                rem //= 10
            if resStr == "":
                return "0"
            return resStr

        acc = []
        pos = 0

        def traverse(index: int) -> int:
            if index >= len(word):
                return index
            currentChar = word[index]

            def innerLoop(j: int, ch: str, ccount: int):
                if j >= len(word) or word[j] != ch or ccount == 9:
                    return j, ccount
                return innerLoop(j + 1, ch, ccount + 1)

            newIndex, finalCount = innerLoop(index, currentChar, 0)
            acc.append(toStr(finalCount) + currentChar)
            return newIndex

        def loop(idx: int) -> None:
            if idx >= len(word):
                return
            nextIdx = traverse(idx)
            loop(nextIdx)

        loop(pos)

        outputStr = ""
        for k in range(len(acc)):
            outputStr += acc[k]

        return outputStr