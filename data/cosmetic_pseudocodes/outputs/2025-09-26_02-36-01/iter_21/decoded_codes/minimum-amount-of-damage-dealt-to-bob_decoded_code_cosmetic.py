class Enemy:
    def __init__(self, damage, timeTakenDown):
        self.damage = damage
        self.timeTakenDown = timeTakenDown


class Solution:
    def minDamage(self, power, damage, health):
        mRYW = 0
        for val in damage:
            mRYW += val

        GvUtZ1p = len(damage)
        hnY8mxI = []
        qrMlhqT = 0
        d2r5j83 = 0

        while True:
            if qrMlhqT < GvUtZ1p:
                PxFWLN = damage[qrMlhqT]
                d2r5j83_health = health[qrMlhqT]
                SiQtCX7 = (d2r5j83_health + power - 1) // power
                hnY8mxI.append(Enemy(PxFWLN, SiQtCX7))
                qrMlhqT += 1
            else:
                break

        # Perform insertion sort on hnY8mxI according to the product comparison
        for i in range(1, len(hnY8mxI)):
            j = i
            while (
                j > 0
                and (hnY8mxI[j - 1].damage * hnY8mxI[j].timeTakenDown) < (hnY8mxI[j].damage * hnY8mxI[j - 1].timeTakenDown)
            ):
                hnY8mxI[j], hnY8mxI[j - 1] = hnY8mxI[j - 1], hnY8mxI[j]
                j -= 1

        j = 0
        while j < len(hnY8mxI):
            d2r5j83 += hnY8mxI[j].timeTakenDown * hnY8mxI[j].damage
            mRYW -= hnY8mxI[j].damage
            j += 1

        return d2r5j83