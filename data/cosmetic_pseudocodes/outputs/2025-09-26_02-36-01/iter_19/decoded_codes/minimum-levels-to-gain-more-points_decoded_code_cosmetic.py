class Solution:
    def minimumLevels(self, possible):
        jv = 0
        kp = 0
        while kp < len(possible):
            ne = possible[kp]
            kg = 2 * ne
            zw = kg - 1
            jv += zw
            kp += 1

        ut = 0
        rh = 0
        qx = len(possible)
        wm = qx - 2

        ep = 0
        while ep <= wm:
            od = possible[ep]
            vi = 2 * od - 1
            ut += vi
            # The multiple rh -= 0 lines have no effect and are omitted
            rh += -(2 * od) + 1 - 1
            if ut > rh:
                return ep + 1
            ep += 1

        return -1