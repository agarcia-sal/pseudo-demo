class Solution:
    def largestSquareArea(self, bottomLeft, topRight):
        def intersecting_square_area(bl1, tr1, bl2, tr2):
            def max_val(a, b):
                return a if a > b else b

            def min_val(a, b):
                return a if a < b else b

            alpha = max_val(bl1[0], bl2[0])
            beta = min_val(tr1[0], tr2[0])
            gamma = max_val(bl1[1], bl2[1])
            delta = min_val(tr1[1], tr2[1])

            if alpha >= beta or gamma >= delta:
                return 0

            epsilon = min_val(beta - alpha, delta - gamma)
            return epsilon * epsilon

        omega = 0
        tau = len(bottomLeft)
        i = 0

        while i < tau:
            j = i + 1
            while True:
                if j >= tau:
                    break
                zeta = intersecting_square_area(bottomLeft[i], topRight[i], bottomLeft[j], topRight[j])
                if zeta > omega:
                    omega = zeta
                j += 1
            i += 1

        return omega