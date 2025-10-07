class Solution:
    def queryResults(self, limit, queries):
        hueMapping = {}
        distinctHues = set()
        tallyList = []

        iteratorIndex = 0
        while iteratorIndex < len(queries):
            pointPair = queries[iteratorIndex]
            firstValue = pointPair[0]
            secondValue = pointPair[1]

            hueExists = False
            if firstValue in hueMapping:
                previousHue = hueMapping[firstValue]
                hueExists = True
            else:
                previousHue = None

            if hueExists:
                if previousHue in distinctHues:
                    distinctHues.remove(previousHue)

            hueMapping[firstValue] = secondValue
            distinctHues.add(secondValue)

            currentCount = len(distinctHues)
            tallyList.append(currentCount)

            iteratorIndex += 1

        return tallyList