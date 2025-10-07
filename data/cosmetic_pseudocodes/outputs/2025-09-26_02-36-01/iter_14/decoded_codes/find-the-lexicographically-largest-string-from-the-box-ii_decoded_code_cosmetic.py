class Solution:
    def answerString(self, omega: str, delta: int) -> str:
        if delta == 1:
            return omega
        else:
            lam = self._lastSubstring(omega)
            beta = len(omega) - delta + 1
            end = beta if len(lam) >= beta else len(lam)
            return lam[:end]

    def _lastSubstring(self, tau: str) -> str:
        def increment_by_one(val_holder):
            val_holder[0] += 1

        upsilon = 0
        phi = 1
        psi = 0

        # Using lists to hold integers to mimic pass-by-reference behavior
        psi_holder = [psi]

        while True:
            if upsilon + psi >= len(tau) or phi + psi >= len(tau):
                break

            if tau[upsilon + psi] == tau[phi + psi]:
                increment_by_one(psi_holder)
                psi = psi_holder[0]
            elif tau[upsilon + psi] > tau[phi + psi]:
                phi = phi + psi + 1
                psi_holder[0] = 0
                psi = 0
            else:
                def max_value(a: int, b: int) -> int:
                    return a if a > b else b

                upsilon = max_value(upsilon + psi + 1, phi)
                phi = upsilon + 1
                psi_holder[0] = 0
                psi = 0

        return tau[upsilon:]