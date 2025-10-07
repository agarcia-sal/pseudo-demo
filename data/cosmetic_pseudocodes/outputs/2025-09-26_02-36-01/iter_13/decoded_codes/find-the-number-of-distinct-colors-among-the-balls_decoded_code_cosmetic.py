class Solution:
    def queryResults(self, limit, queries):
        ballColorsMap = {}
        distinctColorCollection = set()
        outputCounts = []

        def processPair(index):
            if index >= len(queries):
                return
            keyValue, colorValue = queries[index]

            if keyValue in ballColorsMap:
                previousColor = ballColorsMap[keyValue]
                distinctColorCollection.discard(previousColor)

            ballColorsMap[keyValue] = colorValue
            distinctColorCollection.add(colorValue)
            outputCounts.append(len(distinctColorCollection))

            processPair(index + 1)

        processPair(0)
        return outputCounts