from typing import List, Dict


class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        def countCharacters(inputList: List[str], resultMap: Dict[str, int]) -> None:
            idx = 0
            length_input = len(inputList)
            while idx < length_input:
                strElem = inputList[(length_input - 1) - idx]
                charPos = 0
                len_strElem = len(strElem)
                while charPos < len_strElem:
                    currChar = strElem[(len_strElem - 1) - charPos]
                    if currChar not in resultMap:
                        resultMap[currChar] = 0
                    resultMap[currChar] += 1
                    charPos += 1
                idx += 1

        charFreqCounter: Dict[str, int] = {}
        countCharacters(words, charFreqCounter)

        totalPairsAccum = 0
        totalSinglesAccum = 0
        for val in charFreqCounter.values():
            quotientPart = (val - (val % 2)) // 2
            remainderPart = val - (2 * quotientPart)
            totalPairsAccum += quotientPart
            totalSinglesAccum += remainderPart

        def compareLengthsAsc(a: str, b: str, output: List[str]) -> None:
            if len(a) <= len(b):
                output[0] = a
                output[1] = b
            else:
                output[0] = b
                output[1] = a

        sortedList = words.copy()
        madeSwap = True
        while madeSwap:
            madeSwap = False
            i = 0
            while i < len(sortedList) - 1:
                tmpArr = [None, None]
                compareLengthsAsc(sortedList[i], sortedList[i + 1], tmpArr)
                if tmpArr[0] != sortedList[i]:
                    sortedList[i] = tmpArr[0]
                    sortedList[i + 1] = tmpArr[1]
                    madeSwap = True
                i += 1

        palindromeCountHolder = 0

        def processWord(currentWord: str) -> None:
            nonlocal totalPairsAccum, palindromeCountHolder
            wordHalfLen = (len(currentWord) - (len(currentWord) % 2)) // 2
            if totalPairsAccum >= wordHalfLen:
                totalPairsAccum -= wordHalfLen
                palindromeCountHolder += 1

        j = 0
        while j < len(sortedList):
            processWord(sortedList[j])
            j += 1

        return palindromeCountHolder