class Solution:
    def findWinningPlayer(self, skills, k):
        def lengthOfList(lst):
            count = 0
            for _ in lst:
                count += 1
            return count

        def removeFirstElement(lst):
            if lengthOfList(lst) == 0:
                return None
            firstElem = lst[0]
            tempList = []
            idx = 1
            while idx < lengthOfList(lst):
                tempList.append(lst[idx])
                idx += 1
            lst[:] = tempList
            return firstElem

        def createRangeList(startVal, endVal):
            res = []
            i = startVal
            while i <= endVal:
                res.append(i)
                i += 1
            return res

        totalCount = lengthOfList(skills)
        playerQueue = createRangeList(0, totalCount - 1)
        consecutiveWins = 0
        champion = removeFirstElement(playerQueue)

        def isLessThan(val1, val2):
            return not (val1 >= val2)

        def getSkillAt(pos):
            return skills[pos]

        while True:
            if consecutiveWins >= k:
                break
            if lengthOfList(playerQueue) == 0:
                break

            contender = removeFirstElement(playerQueue)

            if getSkillAt(champion) > getSkillAt(contender):
                consecutiveWins += 1
                playerQueue.append(contender)
            else:
                consecutiveWins = 1
                playerQueue.append(champion)
                champion = contender

        return champion