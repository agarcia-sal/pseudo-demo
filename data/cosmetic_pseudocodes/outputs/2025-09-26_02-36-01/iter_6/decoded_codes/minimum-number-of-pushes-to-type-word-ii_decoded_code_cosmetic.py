class Solution:
    def minimumPushes(self, word):
        def countLetters(s):
            letterMap = {}
            indexVar = 0
            length = len(s)
            while indexVar < length:
                currentChar = s[indexVar]
                if currentChar not in letterMap:
                    letterMap[currentChar] = 1
                else:
                    letterMap[currentChar] += 1
                indexVar += 1
            return letterMap

        def sortDescending(values):
            resultList = []
            tempList = list(values)

            def findMax(arr):
                i = 0
                maxVal = -2147483648
                maxIndex = 0
                while i < len(arr):
                    if arr[i] > maxVal:
                        maxVal = arr[i]
                        maxIndex = i
                    i += 1
                return maxIndex

            while len(tempList) > 0:
                pos = findMax(tempList)
                resultList.append(tempList[pos])
                tempList.pop(pos)
            return resultList

        frequencyMap = countLetters(word)
        frequencies = [frequencyMap[key] for key in frequencyMap]
        orderedFreq = sortDescending(frequencies)

        accumPushes = 0
        pressLevel = 1
        assignedCount = 0

        def innerLoop(arr, idx, acc, press, assigned):
            if idx >= len(arr):
                return acc
            currentVal = arr[idx]
            updatedAcc = acc + (currentVal * press)
            updatedAssigned = assigned + 1
            newPress = press
            newAssigned = updatedAssigned
            if updatedAssigned == 8:
                newPress = press + 1
                newAssigned = 0
            return innerLoop(arr, idx + 1, updatedAcc, newPress, newAssigned)

        finalResult = innerLoop(orderedFreq, 0, accumPushes, pressLevel, assignedCount)
        return finalResult