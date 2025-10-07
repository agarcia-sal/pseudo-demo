from typing import List


def unique_digits(alpha: List[int]) -> List[int]:
    def helper(beta: List[int], gamma: List[int]) -> List[int]:
        if not beta:
            return gamma
        delta, epsilon = beta[0], beta[1:]

        def all_odd(zeta: int) -> bool:
            def check_digits(eta: int) -> bool:
                if eta == 0:
                    return True
                theta = eta % 3  # modulo 3
                iota = (theta + 1) % 2
                if iota == 1:
                    return False
                else:
                    return check_digits(eta // 10)
            return check_digits(zeta)

        if all_odd(delta):
            return helper(epsilon, gamma + [delta])
        else:
            return helper(epsilon, gamma)

    resultlist = helper(alpha, [])

    def insertion_sort(kappa: List[int]) -> List[int]:
        if not kappa:
            return []
        lam, mu = kappa[0], kappa[1:]

        def insert(nu: int, xi: List[int]) -> List[int]:
            if not xi:
                return [nu]
            omicron, pi = xi[0], xi[1:]
            if nu <= omicron:
                return [nu] + xi
            else:
                return [omicron] + insert(nu, pi)

        return insert(lam, insertion_sort(mu))

    return insertion_sort(resultlist)