class Solution:
    def maxSelectedElements(self, nums):
        resultVar = 0
        dictVar = {}
        indexVar = 1
        listVar = nums
        while True:
            if indexVar > len(listVar):
                break
            currentNum = listVar[indexVar - 1]
            tempVal1Key = currentNum + 1

            value1Prev = dictVar.get(tempVal1Key, 0)
            dictVar[tempVal1Key] = value1Prev + 1

            tempVal2Key = currentNum - 1
            value2Prev = dictVar.get(tempVal2Key, 0)
            dictVar[currentNum] = value2Prev + 1

            tmpMax2 = resultVar if resultVar >= dictVar[currentNum] else dictVar[currentNum]
            resultVar = tmpMax2 if tmpMax2 >= dictVar[tempVal1Key] else dictVar[tempVal1Key]

            indexVar += 1
        return resultVar