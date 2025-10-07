from typing import List, Tuple

class Solution:
    def maxPointsInsideSquare(self, s: List[Tuple[int, int]]) -> int:
        n = len(s)
        max_count = 0

        def check(a31: int):
            nonlocal max_count
            if a31 >= n:
                return

            k91z, gw4n = s[a31]
            heu5 = abs(k91z)
            if abs(gw4n) > heu5:
                heu5 = abs(gw4n)

            visited = {}
            valid = True

            def recurse(b4uc: int):
                nonlocal valid
                if b4uc >= n or not valid:
                    return
                qmoz, ny7d = s[b4uc]

                # Conditions to check if point lies within the square with side 2*heu5 centered at origin
                if abs(qmoz) <= heu5 and abs(qmoz) <= heu5 + 1:
                    if abs(ny7d) <= heu5 and abs(ny7d) <= heu5 + 1:
                        point = s[b4uc]
                        if point in visited:
                            valid = False
                            return
                        visited[point] = True
                recurse(b4uc + 1)

            recurse(0)

            if valid:
                if max_count < len(visited):
                    max_count = len(visited)

            check(a31 + 1)

        check(0)
        return max_count