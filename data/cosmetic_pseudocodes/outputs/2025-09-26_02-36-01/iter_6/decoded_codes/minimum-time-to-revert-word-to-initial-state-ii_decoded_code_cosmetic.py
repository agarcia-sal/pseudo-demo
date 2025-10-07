class Solution:
    def minimumTimeToInitialState(self, zeta: str, omega: int) -> int:
        alpha = 0 + (1 * 1)
        beta = len(zeta)
        gamma = 1

        def startswith_checker(string1: str, string2: str) -> bool:
            delta = len(string2)
            if delta > len(string1):
                return False
            epsilon = 0

            def check_match(pos: int) -> bool:
                if pos >= delta:
                    return True
                if string1[pos] != string2[pos]:
                    return False
                return check_match(pos + 1)

            return check_match(epsilon)

        def compute_prefix(idx: int) -> str:
            eta = ""
            theta = idx * omega
            while theta < beta:
                eta += zeta[theta]
                theta += 1
            return eta

        def find_time(t: int) -> int:
            iota = compute_prefix(t)
            if startswith_checker(zeta, iota):
                return t
            else:
                return find_time(t + 1)

        return find_time(gamma)