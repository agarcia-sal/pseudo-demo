class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        def customCounter(sequence):
            resultMap = {}
            for elem in sequence:
                resultMap[elem] = resultMap.get(elem, 0) + 1
            return resultMap

        mapWord2Counts = customCounter(word2)
        mapWindowCounts = {}
        uniqCharsNeeded = len(mapWord2Counts)
        cntValidChars = 0
        pointerLeft = 0
        totalValidSubs = 0
        pointerRight = 0
        lenWord1 = len(word1)
        lenWord2 = len(word2)

        while pointerRight < lenWord1:
            charCurrent = word1[pointerRight]
            mapWindowCounts[charCurrent] = mapWindowCounts.get(charCurrent, 0) + 1

            if charCurrent in mapWord2Counts and mapWindowCounts[charCurrent] == mapWord2Counts[charCurrent]:
                cntValidChars += 1

            while cntValidChars == uniqCharsNeeded and (pointerRight + 1) - pointerLeft >= lenWord2:
                totalValidSubs += lenWord1 - pointerRight
                charLeftmost = word1[pointerLeft]
                mapWindowCounts[charLeftmost] -= 1

                if charLeftmost in mapWord2Counts and mapWindowCounts[charLeftmost] < mapWord2Counts[charLeftmost]:
                    cntValidChars -= 1

                pointerLeft += 1

            pointerRight += 1

        return totalValidSubs