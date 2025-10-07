from collections import defaultdict

class Solution:
    def betterCompression(self, compressed: str) -> str:
        charFrequency = defaultdict(int)
        letterHolder = ''
        digitAccumulator = 0
        index = 0
        while index < len(compressed):
            symbol = compressed[index]
            if symbol.isalpha():
                if letterHolder != '':
                    charFrequency[letterHolder] += digitAccumulator
                letterHolder = symbol
                digitAccumulator = 0
            else:
                digitAccumulator = digitAccumulator * 10 + int(symbol)
            index += 1
        if letterHolder != '':
            charFrequency[letterHolder] += digitAccumulator
        partsList = []
        for currentKey in sorted(charFrequency.keys()):
            partsList.append(currentKey + str(charFrequency[currentKey]))
        resultString = ''.join(partsList)
        return resultString