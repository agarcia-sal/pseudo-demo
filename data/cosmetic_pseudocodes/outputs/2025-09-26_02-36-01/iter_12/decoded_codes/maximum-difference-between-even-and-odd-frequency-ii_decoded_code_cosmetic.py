class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        def ComputePairs():
            letters = ["zero", "one", "two", "three", "four"]
            result = []

            def AddPairs(i, j):
                if i >= len(letters):
                    return
                if j >= len(letters):
                    AddPairs(i + 1, i + 2)
                    return
                if letters[i] != letters[j]:
                    result.append((letters[i], letters[j]))
                AddPairs(i, j + 1)

            AddPairs(0, 1)
            return result

        # Large negative number to substitute negative infinity
        answer = -10 ** 10

        pairsList = ComputePairs()

        class CustomDefaultDictWithInfinity:
            def __init__(self):
                self.storage = {}

            def get(self, key):
                return self.storage.get(key, 10 ** 10)

            def set(self, key, value):
                self.storage[key] = value

        def ModTwo(value: int) -> int:
            return value - 2 * (value // 2)

        for x, y in pairsList:
            minD = CustomDefaultDictWithInfinity()
            prefixX = [0]
            prefixY = [0]
            startPtr = 0

            def ProcessIndex(index: int):
                nonlocal startPtr, answer
                ch = s[index]
                if ch == x:
                    prefixX.append(prefixX[-1] + 1)
                else:
                    prefixX.append(0)
                if ch == y:
                    prefixY.append(prefixY[-1] + 1)
                else:
                    prefixY.append(0)

                while (index - startPtr + 1) >= k and prefixX[startPtr] < prefixX[-1] and prefixY[startPtr] < prefixY[-1]:
                    parityKey = (ModTwo(prefixX[startPtr]), ModTwo(prefixY[startPtr]))
                    currentMin = minD.get(parityKey)
                    candidate = prefixX[startPtr] - prefixY[startPtr]
                    if candidate < currentMin:
                        minD.set(parityKey, candidate)
                    startPtr += 1

                lastIndex = len(prefixX) - 1
                queryKey = (ModTwo(1 - ModTwo(prefixX[lastIndex])), ModTwo(prefixY[lastIndex]))
                potentialAns = prefixX[lastIndex] - prefixY[lastIndex] - minD.get(queryKey)
                if potentialAns > answer:
                    answer = potentialAns

            idx = 0

            def IterateOverIndices():
                nonlocal idx
                while idx < len(s):
                    ProcessIndex(idx)
                    idx += 1

            IterateOverIndices()

        return answer