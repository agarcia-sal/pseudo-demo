from collections import defaultdict

class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        output = -(1 << 31)
        pairs = []
        base = ["zero", "one", "two", "three", "four"]
        for i in range(len(base)):
            for j in range(len(base)):
                if i != j:
                    pairs.append((base[i], base[j]))

        for x, y in pairs:
            dictMin = defaultdict(lambda: 1 << 31)
            prefX = [0]
            prefY = [0]
            idxL = 0
            idxR = 0
            while idxR < len(s):
                charCurrent = s[idxR]

                lastPrefX = prefX[-1]
                if charCurrent == x:
                    prefX.append(lastPrefX + 1)
                else:
                    prefX.append(0)

                lastPrefY = prefY[-1]
                if charCurrent == y:
                    prefY.append(lastPrefY + 1)
                else:
                    prefY.append(0)

                while idxR - idxL + 1 >= k and prefX[idxL] < prefX[-1] and prefY[idxL] < prefY[-1]:
                    keyX = prefX[idxL] % 2
                    keyY = prefY[idxL] % 2
                    tKey = (keyX, keyY)
                    candidate = prefX[idxL] - prefY[idxL]
                    if dictMin[tKey] > candidate:
                        dictMin[tKey] = candidate
                    idxL += 1

                curX = prefX[-1]
                curY = prefY[-1]
                key1 = ((1 - (curX % 2)), (curY % 2))
                valCheck = curX - curY - dictMin[key1]
                if valCheck > output:
                    output = valCheck
                idxR += 1

        return output