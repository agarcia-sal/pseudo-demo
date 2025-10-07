from collections import defaultdict

class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        result = - (2 ** 31)
        chars = ["zero", "one", "two", "three", "four"]
        pairs = []
        for i in range(len(chars)):
            for j in range(len(chars)):
                if chars[i] != chars[j]:
                    pairs.append((chars[i], chars[j]))

        for x, y in pairs:
            cache = defaultdict(lambda: 2 ** 31)
            prefixCountX = [0]
            prefixCountY = [0]
            left = 0

            for position, ch in enumerate(s):
                if ch == x:
                    prefixCountX.append(prefixCountX[-1] + 1)
                else:
                    prefixCountX.append(prefixCountX[-1])

                if ch == y:
                    prefixCountY.append(prefixCountY[-1] + 1)
                else:
                    prefixCountY.append(prefixCountY[-1])

                while (position - left + 1) >= k and prefixCountX[left] < prefixCountX[-1] and prefixCountY[left] < prefixCountY[-1]:
                    parityKey = (prefixCountX[left] % 2, prefixCountY[left] % 2)
                    diff = prefixCountX[left] - prefixCountY[left]
                    if cache[parityKey] > diff:
                        cache[parityKey] = diff
                    left += 1

                endX = prefixCountX[-1]
                endY = prefixCountY[-1]
                currentParityKey = ((1 - (endX % 2)), (endY % 2))

                tempDiff = endX - endY - cache[currentParityKey]
                if result < tempDiff:
                    result = tempDiff

        return result