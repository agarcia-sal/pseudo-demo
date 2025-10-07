from typing import List, TypeVar

T = TypeVar('T')

def sort_even(list_of_elements: List[T]) -> List[T]:
    omega: List[T] = []
    alpha: List[T] = []
    idx_phi: int = 0

    while idx_phi < len(list_of_elements):
        # Append elements at even indices to omega, odd indices to alpha
        if idx_phi % 2 == 0:
            omega.append(list_of_elements[idx_phi])
        else:
            alpha.append(list_of_elements[idx_phi])
        idx_phi += 1

    kappa: int = 0
    # Sort omega using a simple selection sort
    while kappa < len(omega) - 1:
        mda = kappa
        while mda < len(omega):
            if omega[mda] < omega[kappa]:
                omega[kappa], omega[mda] = omega[mda], omega[kappa]
            mda += 1
        kappa += 1

    xi: List[T] = []
    rho: int = 0

    # Interleave sorted omega and alpha elements
    while rho < len(alpha) and rho < len(omega):
        xi.append(omega[rho])
        xi.append(alpha[rho])
        rho += 1

    # Append the last element of omega if omega is longer than alpha
    if len(omega) > len(alpha):
        xi.append(omega[-1])

    return xi