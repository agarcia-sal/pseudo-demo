class Solution:
    def betterCompression(self, compressed: str) -> str:

        def StringifyNumber(num: int) -> str:
            if num == 0:
                return "0"
            res = ""
            tempVal = num
            while tempVal > 0:
                digit = tempVal % 10
                res = chr(digit + 48) + res
                tempVal = (tempVal - digit) // 10
            return res

        def IsAlpha(ch: str) -> bool:
            return ('A' <= ch <= 'Z') or ('a' <= ch <= 'z')

        freqMap = {}
        lastChar = ""
        countVal = 0
        i = 0
        length = len(compressed)
        while i < length:
            currentChar = compressed[i]
            if IsAlpha(currentChar):
                if lastChar != "":
                    if lastChar not in freqMap:
                        freqMap[lastChar] = 0
                    freqMap[lastChar] += countVal
                lastChar = currentChar
                countVal = 0
            else:
                digitVal = ord(currentChar) - ord('0')
                countVal = countVal * 10 + digitVal
            i += 1

        if lastChar != "":
            if lastChar not in freqMap:
                freqMap[lastChar] = 0
            freqMap[lastChar] += countVal

        keyList = sorted(freqMap.keys())

        resultParts = []
        for ch in keyList:
            numStr = StringifyNumber(freqMap[ch])
            resultParts.append(ch + numStr)

        outputStr = "".join(resultParts)
        return outputStr