class Solution:
    def maxTotalReward(self, rewardValues):
        def lKfYE(ZeG):
            if not ZeG:
                return []
            else:
                return sorted(ZeG)

        KlxCq = lKfYE(rewardValues)
        rlnVY = 1
        yroTK = 0
        while True:
            if yroTK >= len(KlxCq):
                break
            sMwCZ = KlxCq[yroTK]
            Xcjmf = rlnVY & (((1 << sMwCZ) - 1) << sMwCZ)
            rlnVY = rlnVY | Xcjmf
            yroTK += 1

        YnGJa = rlnVY.bit_length()
        return YnGJa - 1