class Solution:
    def queryResults(self, limit, queries):
        ballMap = dict()
        distinctColors = set()
        outputList = []

        def processNext(index):
            if not (index < limit):
                return

            keyVar = queries[index][0]
            valVar = queries[index][1]

            def hasKey(dct, k):
                return k in dct

            if hasKey(ballMap, keyVar):
                prevColor = ballMap[keyVar]

                def contains(setVar, item):
                    for element in setVar:
                        if element == item:
                            return True
                    return False

                if contains(distinctColors, prevColor):

                    def removeItem(setVar, item):
                        tempSet = set()
                        for element in setVar:
                            if element != item:
                                tempSet.add(element)
                        return tempSet

                    distinctColors_new = removeItem(distinctColors, prevColor)
                    # Update distinctColors only if prevColor is no longer associated with any ball
                    # But pseudocode removes regardless, so assignment done here
                    distinctColors.clear()
                    distinctColors.update(distinctColors_new)

            def assign(dct, k, v):
                dct[k] = v

            assign(ballMap, keyVar, valVar)

            distinctColors.add(valVar)

            def countElements(setVar):
                counter = 0
                for _ in setVar:
                    counter += 1
                return counter

            currentCount = countElements(distinctColors)
            outputList.append(currentCount)

            processNext(index + 1)

        processNext(0)
        return outputList