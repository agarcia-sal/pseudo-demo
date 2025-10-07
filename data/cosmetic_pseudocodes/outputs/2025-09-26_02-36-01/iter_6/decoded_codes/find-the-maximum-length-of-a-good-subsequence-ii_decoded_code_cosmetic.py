from collections import defaultdict

class Solution:
    def maximumLength(self, nums, k):
        totalElements = len(nums)

        def maxValue(a, b):
            return a if a > b else b

        table = []
        dictList = []
        tracker = []
        maxAnswer = 0
        maxKey = k + 1

        for _ in range(totalElements):
            table.append([0] * maxKey)
        for _ in range(maxKey):
            dictList.append(defaultdict(int))
        for _ in range(maxKey):
            tracker.append([0, 0, 0])  # [currentEntry, highest, secondHighest]

        def processIndex(idx):
            nonlocal maxAnswer
            if idx == totalElements:
                return

            currentEntry = nums[idx]

            def iterateH(hValue):
                nonlocal maxAnswer
                if hValue == maxKey:
                    return

                fromDict = dictList[hValue][currentEntry]
                table[idx][hValue] = fromDict

                if hValue > 0:
                    if tracker[hValue - 1][0] != currentEntry:
                        table[idx][hValue] = maxValue(table[idx][hValue], tracker[hValue - 1][1])
                    else:
                        table[idx][hValue] = maxValue(table[idx][hValue], tracker[hValue - 1][2])

                table[idx][hValue] += 1
                dictList[hValue][currentEntry] = maxValue(dictList[hValue][currentEntry], table[idx][hValue])

                if tracker[hValue][0] != currentEntry:
                    if table[idx][hValue] >= tracker[hValue][1]:
                        tracker[hValue][2] = tracker[hValue][1]
                        tracker[hValue][1] = table[idx][hValue]
                        tracker[hValue][0] = currentEntry
                    else:
                        tracker[hValue][2] = maxValue(tracker[hValue][2], table[idx][hValue])
                else:
                    tracker[hValue][1] = maxValue(tracker[hValue][1], table[idx][hValue])

                if maxAnswer < table[idx][hValue]:
                    maxAnswer = table[idx][hValue]

                iterateH(hValue + 1)

            iterateH(0)
            processIndex(idx + 1)

        processIndex(0)
        return maxAnswer