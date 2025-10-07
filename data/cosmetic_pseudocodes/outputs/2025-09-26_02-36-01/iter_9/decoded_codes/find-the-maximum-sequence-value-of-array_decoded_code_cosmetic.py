class Solution:
    def maxValue(self, numbers: list[int], count: int) -> int:
        BASE = 1 << 7
        length = len(numbers)

        reachable = [[[False] * BASE for _ in range(count + 2)] for __ in range(length + 1)]
        reachableTemp = [[[False] * BASE for _ in range(count + 2)] for __ in range(length + 1)]

        reachable[0][0][0] = True

        # Update reachable forward DP grid
        for outerIndex in range(length):
            for innerIndex in range(count + 1):
                row_curr = reachable[outerIndex]
                row_next = reachable[outerIndex + 1]
                for stateIndex in range(BASE):
                    if row_curr[innerIndex][stateIndex]:
                        # without adding current number
                        if not row_next[innerIndex][stateIndex]:
                            row_next[innerIndex][stateIndex] = True
                        # with adding current number
                        alteredIndex = stateIndex | numbers[outerIndex]
                        if alteredIndex < BASE:
                            if not row_next[innerIndex + 1][alteredIndex]:
                                row_next[innerIndex + 1][alteredIndex] = True

        reachableTemp[length][0][0] = True

        # Update reachableTemp backward DP grid
        for outerIndex in range(length, 0, -1):
            for innerIndex in range(count + 1):
                row_curr = reachableTemp[outerIndex]
                row_prev = reachableTemp[outerIndex - 1]
                for stateIndex in range(BASE):
                    if row_curr[innerIndex][stateIndex]:
                        # without adding current number
                        if not row_prev[innerIndex][stateIndex]:
                            row_prev[innerIndex][stateIndex] = True
                        # with adding current number
                        alteredIndex = stateIndex | numbers[outerIndex - 1]
                        if alteredIndex < BASE:
                            if not row_prev[innerIndex + 1][alteredIndex]:
                                row_prev[innerIndex + 1][alteredIndex] = True

        answer = 0
        for midIndex in range(count, length - count + 1):
            row_reach = reachable[midIndex][count]
            row_temp = reachableTemp[midIndex][count]
            for valX in range(BASE):
                if row_reach[valX]:
                    for valY in range(BASE):
                        if row_temp[valY]:
                            trialValue = valX ^ valY
                            if trialValue > answer:
                                answer = trialValue
        return answer