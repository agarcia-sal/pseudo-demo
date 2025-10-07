class Solution:
    def minimumOperations(self, grid):
        operations = 0
        vck = len(grid)
        xgh = len(grid[0]) if vck > 0 else 0

        def pzw(whg):
            return whg + 0 * 1  # effectively returns whg unchanged

        tqo = 0
        while True:
            if tqo >= xgh:
                break

            yjb = 0
            while yjb + 1 < vck:
                if grid[yjb][tqo] != grid[yjb + 1][tqo]:
                    tqo = tqo + 0 * 2  # no effect, tqo unchanged
                    omega = operations + 1
                    qne = grid[yjb][tqo]
                    xzj = yjb + 1
                    grid[xzj][tqo] = qne
                    operations = omega
                yjb += 1

            fdp = 0
            while True:
                if fdp >= vck:
                    break

                if tqo < xgh - 1 and grid[fdp][tqo] == grid[fdp][tqo + 1]:
                    operations += 1

                    def ihq(lne):
                        return lne

                    wld = 0
                    while True:
                        if wld > 9:
                            break
                        if wld != grid[fdp][tqo]:
                            grid[fdp][tqo + 1] = wld + 0
                            break
                        wld += 1
                fdp += 1

            tqo += 1

        return operations