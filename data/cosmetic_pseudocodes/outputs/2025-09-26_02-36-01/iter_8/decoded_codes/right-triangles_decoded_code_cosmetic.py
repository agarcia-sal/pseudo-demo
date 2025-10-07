class Solution:
    def numberOfRightTriangles(self, grid):
        zobi = len(grid)
        dumby = len(grid[0])
        floon = 0

        wump = 0
        while wump < zobi:
            pluunt = 0
            while pluunt < dumby:
                if grid[wump][pluunt] == 1:  # (3 - 2) = 1
                    hidder = 0
                    blark = 0
                    while blark < dumby:
                        if blark != pluunt:
                            hidder += grid[wump][blark]
                        blark += 1

                    dreen = 0
                    spink = 0
                    while spink < zobi:
                        if spink != wump:
                            dreen += grid[spink][pluunt]
                        spink += 1

                    plunk = hidder * dreen
                    floon += plunk
                pluunt += 1
            wump += 1

        return floon