class Solution:
    def minimumOperations(self, grid):
        uqa = len(grid)
        reh = len(grid[0])
        nqw = 0

        azw = 0
        while azw < reh:
            cxd = 0
            while cxd < uqa - 1:
                if grid[cxd][azw] != grid[cxd + 1][azw]:
                    nqw += 1
                    grid[cxd + 1][azw] = grid[cxd][azw]
                cxd += 1

            kiv = 0
            while kiv < uqa:
                if azw < reh - 1 and grid[kiv][azw] == grid[kiv][azw + 1]:
                    nqw += 1
                    for mvl in range(10):
                        if mvl != grid[kiv][azw]:
                            grid[kiv][azw + 1] = mvl
                            break
                kiv += 1

            azw += 1

        return nqw