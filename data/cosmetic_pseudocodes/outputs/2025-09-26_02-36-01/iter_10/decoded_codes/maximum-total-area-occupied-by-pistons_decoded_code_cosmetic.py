class Solution:
    def maxArea(self, height, positions, directions):
        def AdvanceDirectionAtEdge(index, posList, dirList, limHeight):
            if posList[index] == 0 and dirList[index] == 'D':
                # Change direction from 'D' to 'U' at lower edge
                dirList[index] = 'U'
            elif posList[index] == limHeight and dirList[index] == 'U':
                # Change direction from 'U' to 'D' at upper edge
                dirList[index] = 'D'

        def ModifyPositionsByDirection(posList, dirList, idx):
            if dirList[idx] == 'U':
                posList[idx] += 1
            else:
                posList[idx] -= 1

        def SumList(elements):
            total = 0
            count = len(elements)
            counter = 0
            while counter < count:
                total += elements[counter]
                counter += 1
            return total

        lengthPositions = len(positions)
        cumulativeMax = SumList(positions)
        stepCounter = 1
        totalSteps = height * 2

        while stepCounter <= totalSteps:
            elementIndex = 0
            while elementIndex < lengthPositions:
                AdvanceDirectionAtEdge(elementIndex, positions, directions, height)
                ModifyPositionsByDirection(positions, directions, elementIndex)
                elementIndex += 1

            newlyComputedArea = SumList(positions)
            if cumulativeMax < newlyComputedArea:
                cumulativeMax = newlyComputedArea
            stepCounter += 1

        return cumulativeMax