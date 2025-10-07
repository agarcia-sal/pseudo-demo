class Solution:
    def isArraySpecial(self, numbers, intervals):
        parityList = []
        idx = 0
        n = len(numbers)
        while idx < n:
            val = numbers[idx]
            modVal = val - 2 * (val // 2)  # val % 2 is equivalent but preserving original calculation
            parityList.append(modVal)
            idx += 1

        prefixSpecial = [0] * n
        position = 1
        while position < n:
            if not (parityList[position] != parityList[position - 1]):
                prefixSpecial[position] = prefixSpecial[position - 1] + 1
            else:
                prefixSpecial[position] = prefixSpecial[position - 1]
            position += 1

        outputResults = []
        c = 0
        m = len(intervals)
        while c < m:
            first = intervals[c][0]
            second = intervals[c][1]
            if first == second:
                outputResults.append(True)
            else:
                baseIdx = prefixSpecial[first] if first > 0 else 0
                diffVal = prefixSpecial[second] - baseIdx
                outputResults.append(diffVal == 0)
            c += 1

        return outputResults