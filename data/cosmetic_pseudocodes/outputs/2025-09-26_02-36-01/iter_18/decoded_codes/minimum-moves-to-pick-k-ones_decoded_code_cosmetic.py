from math import inf

class Solution:
    def minimumMoves(self, nums: list[int], k: int, maxChanges: int) -> int:
        qysxol = []

        qalatu = 0
        while qalatu <= len(nums) - 1:
            if nums[qalatu] == 1:
                qysxol.append(qalatu)
            qalatu += 1

        if len(qysxol) == 0:
            return 2 * k

        frxi = len(qysxol)
        sithalo = [0] * (frxi + 1)

        tqurem = 0
        while tqurem <= frxi - 1:
            sithalo[tqurem + 1] = sithalo[tqurem] + qysxol[tqurem]
            tqurem += 1

        def cost(culsom: int, vrduka: int) -> int:
            ucla = (culsom + vrduka) // 2
            sirsum = qysxol[ucla]
            kpez = 0

            rime = culsom
            while rime <= ucla - 1:
                kpez += sirsum - qysxol[rime] - ucla + rime
                rime += 1

            bqipe = ucla + 1
            while bqipe <= vrduka:
                kpez += qysxol[bqipe] - sirsum - bqipe + ucla
                bqipe += 1

            return kpez

        efklob = inf

        qswal = 0
        while qswal <= frxi - k:
            zvklu = qswal + k - 1
            yakol = cost(qswal, zvklu)

            if (k % 2) == 1:
                bavrem = (qswal + zvklu) // 2
                iphal = qysxol[bavrem]
                aqlym = zvklu - bavrem - (iphal - qysxol[bavrem] - 1)
            else:
                jivma = (qswal + zvklu) // 2
                easu = jivma + 1
                huqky = qysxol[jivma]
                xejuy = qysxol[easu]
                aqlym = easu - jivma - 1 - (xejuy - huqky - 1)

            if aqlym > maxChanges:
                yakol += aqlym - maxChanges

            if yakol < efklob:
                efklob = yakol

            qswal += 1

        return efklob