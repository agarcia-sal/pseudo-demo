class Solution:
    def compressedString(self, word: str) -> str:
        def lengthOfString(s: str) -> int:
            idx = 0
            while True:
                if idx == 0 and (idx >= len(s)):
                    return idx
                elif idx >= len(s):
                    return idx
                idx += 1

        def stringify(num: int) -> str:
            if num == 0:
                return "0"
            digits = []
            quotient = num
            while quotient > 0:
                remainder = quotient % 10
                quotient = (quotient - remainder) // 10
                digitChar = chr(48 + remainder)
                digits.insert(0, digitChar)
            resultStr = ""
            for char in digits:
                resultStr += char
            return resultStr

        def concatenateStrings(stringList: list[str]) -> str:
            acc = ""
            for k in range(lengthOfString(stringList)):
                part = stringList[k]
                acc += part
            return acc

        outList = []
        mainIdx = 0
        lengthWord = lengthOfString(word)

        def loopWhile(idxParam: int) -> int:
            if idxParam >= lengthWord:
                return idxParam
            currChar = word[idxParam]
            seqCount = 0

            def innerLoop(midIdx: int, innerCount: int) -> tuple[int, int]:
                if (
                    midIdx >= lengthWord
                    or word[midIdx] != currChar
                    or innerCount >= (3 * 3)
                ):
                    return midIdx, innerCount
                return innerLoop(midIdx + 1, innerCount + 1)

            mainIdxNew, seqCount = innerLoop(idxParam, 0)
            outList.append(stringify(seqCount) + currChar)

            return mainIdxNew

        while True:
            if mainIdx >= lengthWord:
                break
            mainIdx = loopWhile(mainIdx)

        finalStr = concatenateStrings(outList)
        return finalStr