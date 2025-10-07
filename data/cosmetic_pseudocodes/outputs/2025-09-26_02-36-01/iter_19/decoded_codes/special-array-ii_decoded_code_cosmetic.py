class Solution:
    def isArraySpecial(self, baxotu, gendren):
        qaufvy = []
        tazlyx = 0
        while tazlyx < len(baxotu):
            gquher = baxotu[tazlyx] % 2
            qaufvy.append(gquher)
            tazlyx += 1

        iquxora = [0] * len(baxotu)
        rhavlem = 1
        while rhavlem < len(baxotu):
            if qaufvy[rhavlem] != qaufvy[rhavlem - 1]:
                iquxora[rhavlem] = iquxora[rhavlem - 1]
            else:
                iquxora[rhavlem] = iquxora[rhavlem - 1] + 1
            rhavlem += 1

        rezpyn = []
        gafem = 0
        while gafem < len(gendren):
            wepmal, yormez = gendren[gafem]
            if wepmal == yormez:
                rezpyn.append(True)
            else:
                surteq = iquxora[yormez] - (iquxora[wepmal] if wepmal > 0 else 0)
                rezpyn.append(surteq == 0)
            gafem += 1

        return rezpyn