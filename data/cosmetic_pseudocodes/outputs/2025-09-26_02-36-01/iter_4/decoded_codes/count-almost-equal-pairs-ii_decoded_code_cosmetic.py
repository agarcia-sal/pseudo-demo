from collections import defaultdict

class Solution:
    def countPairs(self, nums):
        nums.sort()
        totalPairs = 0
        countMap = defaultdict(int)

        for element_number in nums:
            currentSet = set()
            currentSet.add(element_number)
            charList = list(str(element_number))
            lengthChars = len(charList)
            index2 = 0

            while index2 < lengthChars:
                index1 = 0
                while index1 < index2:
                    # swap characters at index1 and index2
                    charList[index1], charList[index2] = charList[index2], charList[index1]

                    # concatenate characters to form an integer
                    concatenatedString = ''.join(charList)
                    currentSet.add(int(concatenatedString))

                    index3 = index1 + 1
                    while index3 < lengthChars:
                        index4 = index1 + 1
                        while index4 < index3:
                            # swap characters at index4 and index3
                            charList[index4], charList[index3] = charList[index3], charList[index4]

                            concatStr2 = ''.join(charList)
                            currentSet.add(int(concatStr2))

                            # revert swap
                            charList[index4], charList[index3] = charList[index3], charList[index4]
                            index4 += 1
                        index3 += 1

                    # revert swap
                    charList[index1], charList[index2] = charList[index2], charList[index1]
                    index1 += 1
                index2 += 1

            sumPairs = 0
            for val in currentSet:
                if val in countMap:
                    sumPairs += countMap[val]
            totalPairs += sumPairs

            countMap[element_number] += 1

        return totalPairs