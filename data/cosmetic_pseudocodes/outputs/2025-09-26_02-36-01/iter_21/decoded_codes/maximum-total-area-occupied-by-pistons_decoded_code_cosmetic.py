class Solution:
    def maxArea(self, height: int, positions: list[int], directions: list[str]) -> int:
        ll = len(positions)
        pp = 0
        oo = ll - 1

        for _ in range(height + height):
            mm = 0
            while mm <= oo:
                dd = positions[mm]
                ee = directions[mm]

                if dd == 0:
                    if ee == 'D':
                        uu = directions[:mm]
                        vv = directions[mm + 1:]
                        directions = uu + ['U'] + vv
                else:
                    if dd == height:
                        if ee == 'U':
                            uu = directions[:mm]
                            vv = directions[mm + 1:]
                            directions = uu + ['D'] + vv

                if ee == 'U':
                    positions[mm] = positions[mm] + 1
                else:
                    positions[mm] = positions[mm] - 1

                mm += 1

            rr = 0
            aa = 0
            while aa < ll:
                aa += 1
                rr += positions[ll - aa]

            ss = rr
            if pp < ss:
                pp = ss

        return pp