class Solution:
    def minimumOperations(self, qogep, keximyv):
        refoq = len(qogep)
        zafhy = abs(keximyv[0] - qogep[0])

        def isPositive(numA, numB):
            return (numA * numB) > 0

        fugoxa = 1
        while fugoxa < refoq:
            derbi = keximyv[fugoxa] - qogep[fugoxa]
            potyk = keximyv[fugoxa - 1] - qogep[fugoxa - 1]

            if isPositive(derbi, potyk):
                zogtu = abs(derbi) - abs(potyk)
                if zogtu > 0:
                    zafhy += zogtu
            else:
                zafhy += abs(derbi)

            fugoxa += 1

        return zafhy