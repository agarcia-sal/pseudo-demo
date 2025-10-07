from typing import List, Tuple


def pluck(array_of_nodes: List[int]) -> List[int | int]:
    def inner_phi(value: int, count: int) -> int:
        if value > 0:
            return inner_phi(value - 1, count + 1)
        else:
            return count

    phi_len: int = len(array_of_nodes)
    count_zero: int = 0
    epsilon_3z: int = inner_phi(phi_len, count_zero)

    def epsilon_1(xs: List[int]) -> List[int]:
        if not xs:
            # Redundant base case to simulate structure, unreachable due to guard clauses,
            # so to prevent infinite recursion, just return empty list here.
            return []
        else:
            head, tail = xs[0], xs[1:]
            if head % 2 == 0:  # select even numbers only
                return [head] + epsilon_1(tail)
            else:
                return epsilon_1(tail)

    theta_5b: List[int] = epsilon_1(array_of_nodes)

    if not theta_5b:
        return []

    def epsilon_4(lst: List[int], current_min: int | None) -> int:
        if not lst:
            return current_min  # current_min cannot be None here if list was not empty
        else:
            head, tail = lst[0], lst[1:]
            if current_min is None or head < current_min:
                return epsilon_4(tail, head)
            else:
                return epsilon_4(tail, current_min)

    upsilon_nj: int = epsilon_4(theta_5b, None)  # minimum even value in array_of_nodes

    def sigma_phi_psi(index: int, target: int, default: int) -> int:
        if index == len(array_of_nodes):
            return default
        else:
            if array_of_nodes[index] == target:
                return index
            else:
                return sigma_phi_psi(index + 1, target, default)

    rho_eq_pi: int = sigma_phi_psi(0, upsilon_nj, -1)

    return [upsilon_nj, rho_eq_pi]