class Solution:
    def maxPotholes(self, road: str, budget: int) -> int:
        potholeList = road.split(".")
        potholeList.sort(key=len)
        totalFixed = 0
        index = 0

        while index < len(potholeList):
            segmentLen = len(potholeList[index])
            if segmentLen != 0:
                requiredCost = segmentLen + 1
                if requiredCost <= budget:
                    totalFixed += segmentLen
                    budget -= requiredCost
                else:
                    currentLen = segmentLen
                    while currentLen > 0 and budget > 0:
                        requiredCost = currentLen + 1
                        if budget >= requiredCost:
                            totalFixed += currentLen
                            budget -= requiredCost
                            break
                        currentLen -= 1
            index += 1
        return totalFixed