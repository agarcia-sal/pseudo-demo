class Solution:
    def countOfPairs(self, nums):
        modVal = 10**9 + 7
        countNums = len(nums)
        highestNum = 0
        idxL = 0
        while idxL < countNums:
            if highestNum < nums[idxL]:
                highestNum = nums[idxL]
            idxL += 1

        def allocate1D(z):
            if z == 0:
                return []
            list1D = [0] * z
            return list1D

        def allocate2D(x, y):
            if x == 0:
                return []
            list2D = []
            iterX = 0
            while iterX < x:
                list2D.append(allocate1D(y))
                iterX += 1
            return list2D

        def allocateDP(size1, size2, size3):
            if size1 == 0:
                return []
            list3D = []
            iter1 = 0
            while iter1 < size1:
                list3D.append(allocate2D(size2, size3))
                iter1 += 1
            return list3D

        dpStructure = allocateDP(countNums + 1, highestNum + 1, highestNum + 1)

        # Initialize dpStructure[1][currentIdx][nums[0] - currentIdx] = 1 for currentIdx in [0..nums[0]]
        def initFirstLevel(currentIdx, limit):
            if currentIdx > limit:
                return
            dpStructure[1][currentIdx][nums[0] - currentIdx] = 1
            initFirstLevel(currentIdx + 1, limit)

        initFirstLevel(0, nums[0])

        # Populate dpStructure for i from 2 to countNums
        def loopI(iVal):
            if iVal > countNums:
                return

            def loopJ(jVal):
                if jVal > nums[iVal - 1]:
                    return

                def loopK(kVal):
                    if kVal > nums[iVal - 1]:
                        return
                    if jVal + kVal == nums[iVal - 1]:

                        def loopPrevJ(pjVal):
                            if pjVal > jVal:
                                return

                            def loopPrevK(pkVal):
                                if pkVal > highestNum:
                                    return
                                oldValue = dpStructure[iVal][jVal][kVal]
                                addValue = dpStructure[iVal - 1][pjVal][pkVal]
                                dpStructure[iVal][jVal][kVal] = (oldValue + addValue) % modVal
                                loopPrevK(pkVal + 1)

                            loopPrevK(kVal)
                            loopPrevJ(pjVal + 1)

                        loopPrevJ(0)
                    loopK(kVal + 1)

                loopK(0)
                loopJ(jVal + 1)

            loopJ(0)
            loopI(iVal + 1)

        loopI(2)

        finalResult = 0

        def sumJ(jVal):
            nonlocal finalResult
            if jVal > highestNum:
                return

            def sumK(kVal):
                nonlocal finalResult
                if kVal > highestNum:
                    return
                tmpSum = dpStructure[countNums][jVal][kVal]
                finalResult = (finalResult + tmpSum) % modVal
                sumK(kVal + 1)

            sumK(0)
            sumJ(jVal + 1)

        sumJ(0)

        return finalResult