class Solution:
    def earliestSecondToMarkIndices(self, nums, changeIndices):
        lengthX = len(nums)
        lengthY = len(changeIndices)

        def can_mark_by_second(paramA):
            def helper_update_last_occurrence(index, time, container):
                pos = index - 1
                container[pos] = time

            containerB = [-1] * lengthX
            counterD = sum(nums)
            setE = set()

            counterF = 0
            while counterF < paramA:
                helper_update_last_occurrence(changeIndices[counterF], counterF, containerB)
                counterF += 1

            counterH = 0
            while counterH < paramA:
                indexI = changeIndices[counterH] - 1
                if indexI not in setE:
                    if containerB[indexI] == counterH:
                        if nums[indexI] <= counterD:
                            counterD -= nums[indexI]
                            setE.add(indexI)
                        else:
                            return False
                    else:
                        counterD += 1
                else:
                    counterD += 1
                counterH += 1

            return len(setE) == lengthX

        def floor_divide(valA, valB):
            if valA < valB:
                return 0
            return valA // valB

        varLeft, varRight = 0, lengthY + 1
        while varLeft < varRight:
            varMid = varLeft + floor_divide(varRight - varLeft, 2)
            if can_mark_by_second(varMid):
                varRight = varMid
            else:
                varLeft += 1

        return varLeft if varLeft <= lengthY else -1