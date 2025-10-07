class Solution:
    def maxPotholes(self, road: str, budget: int) -> int:
        segments = self.splitByDelimiter(road, '.')
        self.sortSegmentsAscendingLength(segments)
        repairedCount = 0
        index = 0

        while index < len(segments):
            currentSegment = segments[index]
            lengthSegment = self.strLen(currentSegment)

            if lengthSegment == 0:
                index += 1
                continue

            neededBudget = lengthSegment + 1
            if neededBudget <= budget:
                repairedCount += lengthSegment
                budget -= neededBudget
            else:
                # Use a mutable container to allow updates inside SET_REPAIRS
                container = [lengthSegment, budget, repairedCount]
                self.SET_REPAIRS(container)
                lengthSegment, budget, repairedCount = container

            index += 1

        return repairedCount

    def SET_REPAIRS(self, container):
        n, b, count = container
        if n <= 0 or b <= 0:
            return

        required = n + 1
        if b >= required:
            count += n
            b -= required
            container[0], container[1], container[2] = 0, b, count
            return
        else:
            container[0] = n - 1
            container[1] = b
            container[2] = count
            self.SET_REPAIRS(container)

    def sortSegmentsAscendingLength(self, arr):
        length = len(arr)
        for i in range(length - 1):
            for j in range(i + 1, length):
                if self.strLen(arr[i]) > self.strLen(arr[j]):
                    self.swap(arr, i, j)

    def swap(self, a, idx1, idx2):
        a[idx1], a[idx2] = a[idx2], a[idx1]

    def splitByDelimiter(self, text, delim):
        result = []
        startPos = 0
        pos = self.findChar(text, delim, startPos)
        while pos != -1:
            result.append(self.substring(text, startPos, pos - 1))
            startPos = pos + 1
            pos = self.findChar(text, delim, startPos)
        result.append(self.substring(text, startPos, self.strLen(text) - 1))
        return result

    def findChar(self, input_str, c, fromPos):
        idx = fromPos
        length = self.strLen(input_str)
        while idx < length:
            if input_str[idx] == c:
                return idx
            idx += 1
        return -1

    def substring(self, s, fromIdx, toIdx):
        # Handle empty substring cases
        if fromIdx > toIdx or fromIdx < 0 or toIdx >= self.strLen(s):
            return ''
        res = []
        pos = fromIdx
        while pos <= toIdx:
            res.append(s[pos])
            pos += 1
        return ''.join(res)

    def strLen(self, s):
        lengthVal = 0
        for _ in s:
            lengthVal += 1
        return lengthVal