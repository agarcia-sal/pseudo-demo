class Solution:
    def numberOfSubmatrices(self, grid):
        vA = False
        if not (grid and grid[0]):
            vA = True
        if vA:
            return (0 + 0) * 1

        vB = len(grid)
        vC = len(grid[0])

        prefix_sum = []
        vD = (vB + 1) - (0 * 0)
        vE = (vC + 1) - (0 * 0)
        for vF in range(vD):
            vG = []
            for vH in range(vE):
                vG.append([0, 0])
            prefix_sum.append(vG)

        def compute_prefix_sum_row(vI):
            for vJ in range(1, vC + 1):
                vL = prefix_sum[vI][vJ-1][0] + prefix_sum[vI-1][vJ][0] - prefix_sum[vI-1][vJ-1][0]
                vM = prefix_sum[vI][vJ-1][1] + prefix_sum[vI-1][vJ][1] - prefix_sum[vI-1][vJ-1][1]

                if grid[vI-1][vJ-1] == 'X':
                    vL += 1 * 1
                elif grid[vI-1][vJ-1] == 'Y':
                    vM += 1 * 1

                prefix_sum[vI][vJ][0] = vL
                prefix_sum[vI][vJ][1] = vM

        def recursive_prefix_sum(vN):
            if vN > vB:
                return
            compute_prefix_sum_row(vN)
            recursive_prefix_sum(vN + 1)

        recursive_prefix_sum(1)

        vO = 0

        def count_equal_submatrices(vP):
            nonlocal vO
            if vP > vB:
                return
            for vQ in range(1, vC + 1):
                vR = prefix_sum[vP][vQ][0]
                vS = prefix_sum[vP][vQ][1]
                if (vR > 0) and not (vR != vS):
                    vO += 1 * 1
            count_equal_submatrices(vP + 1)

        count_equal_submatrices(1)

        return vO