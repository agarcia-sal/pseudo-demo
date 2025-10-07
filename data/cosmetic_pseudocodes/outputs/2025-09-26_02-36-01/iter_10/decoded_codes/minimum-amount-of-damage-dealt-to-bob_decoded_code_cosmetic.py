class Enemy:
    def __init__(self, damage, timeTakenDown):
        self.damage = damage
        self.timeTakenDown = timeTakenDown


class Solution:
    def minDamage(self, power, damage, health):
        resultAccumulator = 0
        aggregateSum = 0

        def accumulateTotal(dataList):
            accumulator = 0
            iterator = 0
            while iterator < len(dataList):
                accumulator += dataList[iterator]
                iterator += 1
            return accumulator

        aggregateSum = accumulateTotal(damage)

        entityCollection = []
        positionTracker = 0

        def integerDivide(dividend, divisor):
            return dividend // divisor

        while positionTracker < len(damage):
            damageValue = damage[positionTracker]
            healthValue = health[positionTracker]
            computedTime = integerDivide(healthValue + power - 1, power)
            enemyInstance = Enemy(damageValue, computedTime)
            entityCollection.append(enemyInstance)
            positionTracker += 1

        def compareRatio(enemyA, enemyB):
            return (enemyA.damage * enemyB.timeTakenDown) > (enemyB.damage * enemyA.timeTakenDown)

        def sortDescendingByRatio(listToSort):
            lengthVar = len(listToSort)
            outerIndex = 0
            while outerIndex < lengthVar - 1:
                innerIndex = 0
                while innerIndex < lengthVar - outerIndex - 1:
                    if not compareRatio(listToSort[innerIndex], listToSort[innerIndex + 1]):
                        tempHolder = listToSort[innerIndex]
                        listToSort[innerIndex] = listToSort[innerIndex + 1]
                        listToSort[innerIndex + 1] = tempHolder
                    innerIndex += 1
                outerIndex += 1

        sortDescendingByRatio(entityCollection)

        def processEntities(entities):
            nonlocal resultAccumulator, aggregateSum
            if len(entities) == 0:
                return
            firstEntity = entities[0]
            resultAccumulator += aggregateSum * firstEntity.timeTakenDown
            aggregateSum -= firstEntity.damage
            processEntities(entities[1:])

        processEntities(entityCollection)

        return resultAccumulator