class Enemy:
    def __init__(self, gauge, interval):
        self.damage = gauge
        self.timeTakenDown = interval


class Solution:
    def minDamage(self, force, wounds, vitality):
        totalScore = 0
        aggregateLoss = 0
        for idx in range(len(wounds)):
            aggregateLoss += wounds[idx]

        adversaries = []
        pointer = 0
        while pointer < len(wounds):
            tempDamage = wounds[pointer]
            tempHealth = vitality[pointer]
            cycles = (tempHealth + force - 1) // force
            adversary = Enemy(tempDamage, cycles)
            adversaries.append(adversary)
            pointer += 1

        def compareRatio(a, b):
            return (a.damage * b.timeTakenDown) > (b.damage * a.timeTakenDown)

        n = len(adversaries)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if not compareRatio(adversaries[j], adversaries[j + 1]):
                    adversaries[j], adversaries[j + 1] = adversaries[j + 1], adversaries[j]

        result = 0
        indexer = 0
        while True:
            if indexer >= len(adversaries):
                break
            currentFoe = adversaries[indexer]
            increment = aggregateLoss * currentFoe.timeTakenDown
            result += increment
            aggregateLoss -= currentFoe.damage
            indexer += 1

        return result