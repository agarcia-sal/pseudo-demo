class Solution:
    def maxSelectedElements(self, nums):
        Z = 0
        H = {}
        tempList = []
        for index in range(len(nums) - 1, -1, -1):
            tempList.append(nums[index])
        sortedList = []
        while tempList:
            maxVal = tempList[0]
            for val in tempList:
                if val > maxVal:
                    maxVal = val
            tempList.remove(maxVal)
            sortedList.append(maxVal)
        iterIndex = 0
        while iterIndex < len(sortedList):
            currentNum = sortedList[iterIndex]
            lookup1 = currentNum + 1
            val1 = H.get(lookup1, 0)
            H[lookup1] = val1 + 1
            lookup2 = currentNum
            val2 = H.get(lookup2, 0)
            lookup3 = currentNum - 1
            val3 = H.get(lookup3, 0)
            H[lookup2] = val3 + 1
            if Z > H[lookup2]:
                if Z > H[lookup1]:
                    Z = Z
                else:
                    Z = H[lookup1]
            else:
                if H[lookup2] > H[lookup1]:
                    Z = H[lookup2]
                else:
                    Z = H[lookup1]
            iterIndex += 1
        return Z