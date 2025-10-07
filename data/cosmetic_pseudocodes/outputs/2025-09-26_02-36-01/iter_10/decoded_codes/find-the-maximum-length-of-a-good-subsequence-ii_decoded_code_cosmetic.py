from collections import defaultdict

class Solution:
    def maximumLength(self, nums, k):
        lengthsCount = len(nums)
        dpTable = [[0] * (k + 1) for _ in range(lengthsCount)]
        memoMaps = [defaultdict(int) for _ in range(k + 1)]
        tracker = [[0, 0, 0] for _ in range(k + 1)]
        maxAnswer = 0

        def iterateIndices(currentIndex):
            nonlocal maxAnswer
            if currentIndex == lengthsCount:
                return

            currentVal = nums[currentIndex]
            for h in range(k + 1):
                valAtIndex = currentIndex
                val = currentVal
                valAtDp = memoMaps[h].get(val, 0)
                dpTable[valAtIndex][h] = valAtDp

                if h > 0:
                    if tracker[h - 1][0] != nums[valAtIndex]:
                        dpTable[valAtIndex][h] = max(dpTable[valAtIndex][h], tracker[h - 1][1])
                    else:
                        dpTable[valAtIndex][h] = max(dpTable[valAtIndex][h], tracker[h - 1][2])

                dpTable[valAtIndex][h] += 1
                memoMaps[h][nums[valAtIndex]] = max(memoMaps[h][nums[valAtIndex]], dpTable[valAtIndex][h])

                if tracker[h][0] != val:
                    if dpTable[valAtIndex][h] >= tracker[h][1]:
                        tracker[h][2] = tracker[h][1]
                        tracker[h][1] = dpTable[valAtIndex][h]
                        tracker[h][0] = val
                    else:
                        tracker[h][2] = max(tracker[h][2], dpTable[valAtIndex][h])
                else:
                    tracker[h][1] = max(tracker[h][1], dpTable[valAtIndex][h])

                maxAnswer = max(maxAnswer, dpTable[valAtIndex][h])

            iterateIndices(currentIndex + 1)

        iterateIndices(0)
        return maxAnswer