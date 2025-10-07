from collections import defaultdict

class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        zeta = 0
        omega = defaultdict(int)
        phi = 0
        psi = 0

        while psi < len(s):
            u = s[psi]
            omega[u] += 1

            while True:
                flag = False
                for key in omega:
                    if omega[key] >= k:
                        flag = True
                        break
                if not flag:
                    break
                v = s[zeta]
                omega[v] -= 1
                if omega[v] == 0:
                    del omega[v]
                zeta += 1

            phi += zeta
            psi += 1

        return phi