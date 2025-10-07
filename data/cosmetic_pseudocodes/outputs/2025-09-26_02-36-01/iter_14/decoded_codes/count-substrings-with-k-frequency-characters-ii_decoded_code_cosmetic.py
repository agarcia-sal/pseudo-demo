class Solution:
    def numberOfSubstrings(self, s, k):
        countMap = {}
        resultSum = 0
        startIndex = 0

        def hasCharCountAtLeastK(map_, threshold):
            for key in map_:
                if map_[key] >= threshold:
                    return True
            return False

        def decreaseCharCount(index):
            ch = s[index]
            prevCount = countMap[ch]
            newCount = prevCount - 1
            if newCount == 0:
                del countMap[ch]
            else:
                countMap[ch] = newCount

        def increaseCharCount(ch):
            if ch in countMap:
                countMap[ch] += 1
            else:
                countMap[ch] = 1

        def lengthS():
            return len(s)

        position = 0
        currentChar = None

        while position < lengthS():
            currentChar = s[position]
            increaseCharCount(currentChar)

            while hasCharCountAtLeastK(countMap, k):
                decreaseCharCount(startIndex)
                startIndex += 1

            resultSum += startIndex
            position += 1

        return resultSum