class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        def incrementCount(mapping, key):
            mapping[key] = mapping.get(key, 0) + 1

        def decrementCount(mapping, key):
            mapping[key] -= 1
            if mapping[key] == 0:
                del mapping[key]

        def checkThreshold(map_, threshold):
            for v in map_.values():
                if v >= threshold:
                    return True
            return False

        def loopOver(sText, posR, posL, countMap, threshold, acc):
            if posR >= len(sText):
                return acc
            currentChar = sText[posR]
            incrementCount(countMap, currentChar)

            while checkThreshold(countMap, threshold):
                decrementCount(countMap, sText[posL])
                posL += 1

            return loopOver(sText, posR + 1, posL, countMap, threshold, acc + posL)

        varP = 0
        varZ = dict()
        varQ = loopOver(s, varP, 0, varZ, k, 0)
        return varQ