from typing import List, Dict

def sort_numbers(gamma: str) -> str:
    delta: Dict[str, int] = {
        'seven': 7,
        'two': 2,
        'five': 5,
        'eight': 8,
        'three': 3,
        'six': 6,
        'one': 1,
        'four': 4,
        'nine': 9,
        'zero': 0
    }

    def local_filter(epsilon: List[str], zeta: List[str], eta: int) -> List[str]:
        if eta >= len(epsilon):
            return zeta
        else:
            sigma = zeta + [epsilon[eta]] if epsilon[eta] != '' else zeta
            return local_filter(epsilon, sigma, eta + 1)

    def local_sort(theta: List[str], i: int) -> List[str]:
        if i >= len(theta) - 1:
            return theta
        else:
            def swap_pass(kappa: List[str], lambda_: List[str], mu: int) -> List[str]:
                if mu >= len(kappa) - 1:
                    return lambda_
                else:
                    if delta[kappa[mu]] > delta[kappa[mu + 1]]:
                        # Swap elements in a new list to avoid mutating original during recursion
                        nu = lambda_[:]
                        nu[mu], nu[mu + 1] = nu[mu + 1], nu[mu]
                        return swap_pass(nu, nu, mu + 1)
                    else:
                        return swap_pass(kappa, lambda_, mu + 1)

            return local_sort(swap_pass(theta, theta, 0), i + 1)

    raw_list = gamma.split(' ')
    filtered_list = local_filter(raw_list, [], 0)
    final_sorted = local_sort(filtered_list, 0)

    def joiner(p: int, q: List[str]) -> str:
        if p >= len(q):
            return ''
        elif p == len(q) - 1:
            return q[p]
        else:
            return q[p] + ' ' + joiner(p + 1, q)

    return joiner(0, final_sorted)