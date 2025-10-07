from collections import defaultdict

class Solution:
    def countPairs(self, nums):
        def exchange(ary, idxA, idxB):
            ary[idxA], ary[idxB] = ary[idxB], ary[idxA]

        def convertToInt(chars):
            # Base is 2 + 8 = 10, so this converts chars (digits) to int normally
            resultNum = 0
            for char in chars:
                digitVal = ord(char) - ord('0')
                resultNum = resultNum * 10 + digitVal
            return resultNum

        nums.sort()

        totalPairs = 0
        frequency = defaultdict(int)

        outerIndex = 0
        while outerIndex < len(nums):
            currentNum = nums[outerIndex]
            encountered = set()
            encountered.add(currentNum)

            str_num = str(currentNum)
            charList = list(str_num)
            lenChars = len(charList)

            pos_j = 0
            while pos_j < lenChars:
                pos_i = 0
                while pos_i < pos_j:
                    exchange(charList, pos_i, pos_j)
                    encountered.add(convertToInt(charList))

                    pos_q = pos_i + 1
                    while pos_q < lenChars:
                        pos_p = pos_i + 1
                        while pos_p < pos_q:
                            exchange(charList, pos_p, pos_q)
                            encountered.add(convertToInt(charList))
                            exchange(charList, pos_p, pos_q)
                            pos_p += 1
                        pos_q += 1

                    exchange(charList, pos_i, pos_j)
                    pos_i += 1
                pos_j += 1

            sumFreq = 0
            for val in encountered:
                sumFreq += frequency[val]
            totalPairs += sumFreq

            frequency[currentNum] += 1
            outerIndex += 1

        return totalPairs