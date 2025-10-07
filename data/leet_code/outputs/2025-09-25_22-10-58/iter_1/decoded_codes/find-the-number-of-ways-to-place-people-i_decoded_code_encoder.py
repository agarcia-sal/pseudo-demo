class Solution:
    def numberOfPairs(self, points):
        count = 0
        n = len(points)
        for i in range(n):
            for j in range(n):
                if i != j:
                    xi, yi = points[i]
                    xj, yj = points[j]
                    if xi <= xj and yi >= yj:
                        valid = True
                        for k in range(n):
                            if k != i and k != j:
                                xk, yk = points[k]
                                if xi <= xk <= xj and yi >= yk >= yj:
                                    valid = False
                                    break
                        if valid:
                            count += 1
        return count