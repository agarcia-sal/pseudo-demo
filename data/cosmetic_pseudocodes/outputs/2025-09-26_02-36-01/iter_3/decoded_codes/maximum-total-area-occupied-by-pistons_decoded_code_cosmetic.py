class Solution:
    def maxArea(self, height: int, positions: list[int], directions: list[str]) -> int:
        nVar = len(positions)
        posList = positions[:]
        dirList = directions[:]

        maxValue = sum(posList)
        counter = 1
        maxCounter = height * 2

        while counter <= maxCounter:
            for idx in range(nVar):
                posVal = posList[idx]
                dirVal = dirList[idx]

                if posVal == 0 and dirVal == 'D':
                    dirList[idx] = 'U'
                elif posVal == height and dirVal == 'U':
                    dirList[idx] = 'D'

                if dirList[idx] == 'U':
                    posList[idx] += 1
                else:
                    posList[idx] -= 1

            tempArea = sum(posList)
            if tempArea > maxValue:
                maxValue = tempArea

            counter += 1

        return maxValue