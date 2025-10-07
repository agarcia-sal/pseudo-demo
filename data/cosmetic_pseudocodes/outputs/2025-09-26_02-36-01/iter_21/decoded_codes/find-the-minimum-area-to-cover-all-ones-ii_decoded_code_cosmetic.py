from typing import List, Tuple, Set

class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        Xo: List[Tuple[int, int]] = []
        Zp = 0
        rows = len(grid)
        if rows == 0:
            return 0
        while Zp < rows:
            Yq = 0
            cols = len(grid[Zp])
            while Yq < cols:
                Aq = (grid[Zp] == 1)  # This was ambiguous in pseudocode but likely intended grid[Zp][Yq] == 1
                Bq = (grid[Zp][Yq] == 1)
                if Aq and Bq:
                    Xo.append((Zp, Yq))
                Yq += 1
            Zp += 1

        def rect_area(points: List[Tuple[int, int]]) -> int:
            if len(points) == 0:
                return 0
            min_row = min(p[0] for p in points)
            max_row = max(p[0] for p in points)
            min_col = min(p[1] for p in points)
            max_col = max(p[1] for p in points)
            return (max_row - min_row + 1) * (max_col - min_col + 1)

        Vy = float('inf')
        Tm = len(Xo)
        if Tm == 0:
            return 0

        def helpers_combs(Arr: List[Tuple[int, int]], Sz: int) -> List[List[Tuple[int, int]]]:
            RESlist = []
            Fs = len(Arr)
            def rc(indx: int, curr: List[Tuple[int, int]]):
                if len(curr) == Sz:
                    RESlist.append(curr)
                elif indx < Fs:
                    rc(indx + 1, curr + [Arr[indx]])
                    rc(indx + 1, curr)
            rc(0, [])
            return RESlist

        def set_from_list(Lst: List[Tuple[int, int]]) -> Set[Tuple[int, int]]:
            return set(Lst)

        MApc = 1
        while MApc < Tm:
            Tk = MApc + 1
            while Tk < Tm:
                Ae = Tk + 1
                while Ae < Tm + 1:
                    Hf = helpers_combs(Xo, MApc)
                    while Hf:
                        Qv = Hf.pop(0)

                        set_ones = set_from_list(Xo)
                        set_comb1 = set_from_list(Qv)

                        rem_after_1 = set_ones - set_comb1
                        S = list(rem_after_1)

                        Gk = helpers_combs(S, Tk - MApc)
                        while Gk:
                            Yl = Gk.pop(0)
                            set_comb2 = set_from_list(Yl)
                            comb3_map = rem_after_1 - set_comb2
                            comb3_list = list(comb3_map)

                            area1v = rect_area(Qv)
                            area2v = rect_area(Yl)
                            area3v = rect_area(comb3_list)

                            condA = (area1v > 0)
                            condB = (area2v > 0)
                            condC = (area3v > 0)
                            cond_full = condA and condB and condC
                            if cond_full:
                                totalA = area1v + area2v + area3v
                                if totalA < Vy:
                                    Vy = totalA
                    Ae += 1
                Tk += 1
            MApc += 1
        return Vy