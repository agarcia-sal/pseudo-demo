class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        mappingCount = {}
        resultTotal = 0
        leftIndex = 0
        rightIndex = 0

        while rightIndex < len(s):
            currentChar = s[rightIndex]
            if currentChar in mappingCount:
                mappingCount[currentChar] += 1
            else:
                mappingCount[currentChar] = 1

            while True:
                existsWithCountToK = False
                for characterX in mappingCount:
                    if mappingCount[characterX] >= k:
                        existsWithCountToK = True
                        break
                if not existsWithCountToK:
                    break

                leftChar = s[leftIndex]
                mappingCount[leftChar] -= 1
                if mappingCount[leftChar] == 0:
                    del mappingCount[leftChar]
                leftIndex += 1

            resultTotal += leftIndex
            rightIndex += 1

        return resultTotal