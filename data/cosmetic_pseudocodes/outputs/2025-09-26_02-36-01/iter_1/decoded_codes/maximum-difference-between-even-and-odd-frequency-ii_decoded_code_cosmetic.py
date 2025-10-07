import math
from collections import defaultdict

class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        result = float('-inf')
        chars = ['zero', 'one', 'two', 'three', 'four']

        for x in chars:
            for y in chars:
                if x != y:
                    mapMinDiff = defaultdict(lambda: math.inf)
                    prefixX = [0]
                    prefixY = [0]
                    start = 0
                    for index, char in enumerate(s):
                        prefixX.append(prefixX[-1] + 1 if char == x else 0)
                        prefixY.append(prefixY[-1] + 1 if char == y else 0)

                        while (index - start + 1) >= k and prefixX[start] < prefixX[-1] and prefixY[start] < prefixY[-1]:
                            key = (prefixX[start] % 2, prefixY[start] % 2)
                            mapMinDiff[key] = min(mapMinDiff[key], prefixX[start] - prefixY[start])
                            start += 1

                        currentKey = ((1 - (prefixX[-1] % 2)), prefixY[-1] % 2)
                        candidate = prefixX[-1] - prefixY[-1] - mapMinDiff[currentKey]
                        if candidate > result:
                            result = candidate

        return result