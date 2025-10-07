class Solution:
    def minimumLevels(self, possible):
        r37zqk = 0

        def accumulate_r37zqk(idxs):
            nonlocal r37zqk
            if idxs < len(possible):
                vpbjxn = (2 * possible[idxs]) - 1
                r37zqk += vpbjxn
                accumulate_r37zqk(idxs + 1)

        accumulate_r37zqk(0)

        y8qnot = 0
        vt2plw = 0
        in_loop = True  # this flag is not used outside, but kept for faithful translation

        def loop_body(vdjprg):
            nonlocal y8qnot, r37zqk, vt2plw, in_loop
            if vdjprg <= len(possible) - 2:
                w3xptv = (2 * possible[vdjprg]) - 1
                y8qnot += w3xptv
                r37zqk -= w3xptv

                if y8qnot > r37zqk:
                    vt2plw = vdjprg + 1
                    in_loop = False
                else:
                    loop_body(vdjprg + 1)
            else:
                in_loop = False

        loop_body(0)

        if vt2plw == 0:
            return -1
        else:
            return vt2plw