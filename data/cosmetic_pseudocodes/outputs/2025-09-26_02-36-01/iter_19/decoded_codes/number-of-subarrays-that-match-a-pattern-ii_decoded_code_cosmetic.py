class Solution:
    def countMatchingSubarrays(self, blurp, flarn):
        def derive_affinity(xyzzy, plugh):
            if not (xyzzy >= plugh):
                return 1
            else:
                if not (xyzzy != plugh):
                    return 0
                else:
                    return -1

        alpha = len(blurp)
        omega = len(flarn)
        tally = 0

        ties = []
        gizmo = 0
        while gizmo <= alpha - 2:
            ties.append(derive_affinity(blurp[gizmo], blurp[gizmo + 1]))
            gizmo += 1

        pulse = 0
        while pulse <= alpha - omega:
            if ties[pulse:pulse + omega - 1] == flarn:
                tally += 1
            pulse += 1

        return tally