class Solution:
    def countPairs(self, nums):
        self.ReorderNumbersInPlace(nums)
        totalPairs = 0
        frequencyMap = self.NewDefaultDict(0)
        for number in nums:
            encounteredSet = self.NewSetWithSingleElement(number)
            digitCharacters = self.ConvertNumberToCharList(number)
            lengthDigits = self.GetListLength(digitCharacters)
            self.EnumerateSwaps(digitCharacters, lengthDigits, encounteredSet)
            totalPairs += self.SumFrequencyMatches(frequencyMap, encounteredSet)
            self.IncrementFrequency(frequencyMap, number)
        return totalPairs

    def ReorderNumbersInPlace(self, listRef):
        n = self.GetListLength(listRef)
        index = 1
        while index < n:
            current = listRef[index]
            position = index - 1
            while position >= 0 and listRef[position] > current:
                listRef[position + 1] = listRef[position]
                position -= 1
            listRef[position + 1] = current
            index += 1

    def NewDefaultDict(self, defaultVal):
        internalMap = {}

        class DefaultDictWrapper:
            def __init__(self, map_, default_):
                self.internalMap = map_
                self.defaultVal = default_

            def getValue(self, key):
                if key in self.internalMap:
                    return self.internalMap[key]
                else:
                    return self.defaultVal

            def setValue(self, key, val):
                self.internalMap[key] = val

            def containsKey(self, key):
                return key in self.internalMap

        return DefaultDictWrapper(internalMap, defaultVal)

    def NewSetWithSingleElement(self, element):
        newSet = set()
        newSet.add(element)
        return newSet

    def ConvertNumberToCharList(self, num):
        chars = []
        numString = self.IntToStr(num)
        str_len = self.GetStringLength(numString)
        for idx in range(str_len):
            chars.append(numString[idx])
        return chars

    def GetListLength(self, lst):
        count = 0
        for _ in lst:
            count += 1
        return count

    def GetStringLength(self, string):
        count = 0
        while True:
            try:
                _ = string[count]
            except IndexError:
                break
            count += 1
        return count

    def IntToStr(self, number):
        if number == 0:
            return "0"
        negativeFlag = False
        if number < 0:
            negativeFlag = True
            number = -number
        digitsList = []
        while number > 0:
            r = number % 10
            number //= 10
            digitsList.append(self.CharFromDigit(r))
        self.ReverseListInPlace(digitsList)
        resultStr = self.JoinChars(digitsList)
        if negativeFlag:
            return "-" + resultStr
        else:
            return resultStr

    def CharFromDigit(self, d):
        digitToCharMap = {0:"0",1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9"}
        return digitToCharMap[d]

    def ReverseListInPlace(self, lst):
        start = 0
        end = self.GetListLength(lst) - 1
        while start < end:
            temp = lst[start]
            lst[start] = lst[end]
            lst[end] = temp
            start += 1
            end -= 1

    def JoinChars(self, chars):
        output = ""
        for c in chars:
            output += c
        return output

    def EnumerateSwaps(self, charList, lengthList, containerSet):
        outerIndex = 0
        while outerIndex <= lengthList - 1:
            middleIndex = 0
            while middleIndex <= outerIndex - 1:
                self.SwapElements(charList, middleIndex, outerIndex)
                self.AddPermutationToSet(charList, containerSet)
                self.EnumerateFurtherSwaps(charList, middleIndex, lengthList, containerSet)
                self.SwapElements(charList, middleIndex, outerIndex)
                middleIndex += 1
            outerIndex += 1

    def SwapElements(self, arr, idx1, idx2):
        tempValue = arr[idx1]
        arr[idx1] = arr[idx2]
        arr[idx2] = tempValue

    def AddPermutationToSet(self, charArray, targetSet):
        convertedNumber = self.StrToInt(self.JoinChars(charArray))
        targetSet.add(convertedNumber)

    def EnumerateFurtherSwaps(self, charArray, startIndex, lengthList, targetSet):
        endIndex = startIndex + 1
        while endIndex <= lengthList - 1:
            midIndex = startIndex + 1
            while midIndex <= endIndex - 1:
                self.SwapElements(charArray, midIndex, endIndex)
                self.AddPermutationToSet(charArray, targetSet)
                self.SwapElements(charArray, midIndex, endIndex)
                midIndex += 1
            endIndex += 1

    def StrToInt(self, strVal):
        negativeFlag = False
        idx = 0
        lengthStr = self.GetStringLength(strVal)
        if lengthStr > 0 and strVal[0] == '-':
            negativeFlag = True
            idx = 1
        resultNum = 0
        while idx < lengthStr:
            digitValue = self.DigitFromChar(strVal[idx])
            resultNum = resultNum * 10 + digitValue
            idx += 1
        if negativeFlag:
            return -resultNum
        else:
            return resultNum

    def DigitFromChar(self, character):
        charToDigitMap = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
        return charToDigitMap[character]

    def SumFrequencyMatches(self, freqMap, elementsSet):
        totalSum = 0
        for element in elementsSet:
            if freqMap.containsKey(element):
                totalSum += freqMap.getValue(element)
        return totalSum

    def IncrementFrequency(self, freqMap, keyVal):
        if freqMap.containsKey(keyVal):
            freqMap.internalMap[keyVal] = freqMap.getValue(keyVal) + 1
        else:
            freqMap.internalMap[keyVal] = 1