from collections import defaultdict

class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        result = -1 << 60
        digits = "01234"
        pairs = []
        for i in range(len(digits)):
            for j in range(len(digits)):
                if digits[i] != digits[j]:
                    pairs.append((digits[i], digits[j]))

        idx = 0
        while idx < len(pairs):
            x, y = pairs[idx]
            lowestDiff = defaultdict(lambda: 1 << 60)
            countX = [0]
            countY = [0]
            start = 0
            for pos in range(len(s)):
                if s[pos] == x:
                    countX.append(countX[-1] + 1)
                else:
                    countX.append(0)
                if s[pos] == y:
                    countY.append(countY[-1] + 1)
                else:
                    countY.append(0)

                while (pos - start + 1) >= k and countX[start] < countX[-1] and countY[start] < countY[-1]:
                    parityKey = (countX[start] % 2, countY[start] % 2)
                    lowestDiff[parityKey] = min(lowestDiff[parityKey], countX[start] - countY[start])
                    start += 1

                currentParity = ((1 - (countX[-1] % 2)), (countY[-1] % 2))
                candidate = (countX[-1] - countY[-1]) - lowestDiff[currentParity]
                if candidate > result:
                    result = candidate
            idx += 1

        return result