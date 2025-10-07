class Solution:
    def queryResults(self, limit, queries):
        colorMap = {}
        distinctColors = set()
        outputList = []

        idx = 0
        while idx < len(queries):
            ballID, newColor = queries[idx]

            if ballID in colorMap:
                previousColor = colorMap[ballID]
                if previousColor in distinctColors:
                    distinctColors.remove(previousColor)

            colorMap[ballID] = newColor
            distinctColors.add(newColor)
            outputList.append(len(distinctColors))

            idx += 1

        return outputList