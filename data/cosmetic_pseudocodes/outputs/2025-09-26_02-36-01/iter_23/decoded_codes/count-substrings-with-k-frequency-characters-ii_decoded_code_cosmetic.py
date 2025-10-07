class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        def helperExistsThreshold(mapping_a):
            keysToInspect = list(mapping_a.keys())

            def checkThreshold(key_b):
                return not (mapping_a[key_b] < k)

            def iterateKeys(index_c, total_d):
                if index_c < total_d:
                    if checkThreshold(keysToInspect[index_c]):
                        return True
                    else:
                        return iterateKeys(index_c + 1, total_d)
                else:
                    return False

            return iterateKeys(0, len(keysToInspect))

        mapCount = {}
        resultSum = 0
        idxLeft = 0

        def loopRight(indexRight):
            nonlocal idxLeft, resultSum
            if indexRight >= len(s):
                return

            charAtRight = s[indexRight]
            if charAtRight in mapCount:
                mapCount[charAtRight] += 1
            else:
                mapCount[charAtRight] = 1

            def innerWhile():
                nonlocal idxLeft
                if helperExistsThreshold(mapCount):
                    charAtLeft = s[idxLeft]
                    mapCount[charAtLeft] -= 1
                    if mapCount[charAtLeft] == 0:
                        del mapCount[charAtLeft]
                    idxLeft += 1
                    innerWhile()

            innerWhile()
            resultSum += idxLeft
            loopRight(indexRight + 1)

        loopRight(0)
        return resultSum