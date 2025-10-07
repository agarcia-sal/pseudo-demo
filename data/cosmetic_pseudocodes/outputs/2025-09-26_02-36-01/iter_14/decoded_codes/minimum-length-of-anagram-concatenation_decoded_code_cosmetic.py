class Solution:
    def minAnagramLength(self, s):
        def buildCharSet(t):
            resultSet = set()
            index = 0
            while index < len(t):
                currChar = t[index]
                if currChar not in resultSet:
                    resultSet.add(currChar)
                index += 1
            return resultSet

        allFound = buildCharSet(s)
        totalCount = 0
        for keyChar in allFound:
            totalCount += 1
        return totalCount