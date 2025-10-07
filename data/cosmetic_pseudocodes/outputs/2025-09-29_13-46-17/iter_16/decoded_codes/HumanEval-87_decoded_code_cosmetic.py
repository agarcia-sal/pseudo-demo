from typing import List, Set, Tuple


def get_row(two_dimensional_list: List[List[int]], target_integer: int) -> List[Tuple[int, int]]:
    found_positions: Set[Tuple[int, int]] = set()

    # Recursive lambda-like function to scan rows and columns
    def scan(i: int, j: int, k) -> None:
        if i < 0:
            return
        # Inner recursion over columns
        def scan_cols(x: int, y, z):
            if x < 0:
                # Move to next row upwards
                return scan(i - 1, len(two_dimensional_list[i - 1]) - 1 if i - 1 >= 0 else -1, None)
            if two_dimensional_list[i][x] != target_integer:
                # If not target, move left
                return scan_cols(x - 1, y, z)
            # If target found, add position and move left
            found_positions.add((i, x))
            return scan_cols(x - 1, y, z)
        scan_cols(len(two_dimensional_list[i]) - 1, None, None)

    # Start scanning from last row and last column index
    scan(len(two_dimensional_list) - 1,
         len(two_dimensional_list[-1]) - 1 if two_dimensional_list else -1,
         None)

    positions = list(found_positions)

    # Comparator τ: sort ascending by column index
    def tau(a: Tuple[int, int], b: Tuple[int, int]) -> int:
        return -1 if a[1] < b[1] else 1 if a[1] > b[1] else 0

    # Comparator σ: sort descending by row index
    def sigma(a: Tuple[int, int], b: Tuple[int, int]) -> int:
        return -1 if a[0] > b[0] else 1 if a[0] < b[0] else 0

    # Selection sort positions by ascending column (tau)
    tau_sorted = []
    while positions:
        min_idx = 0
        for idx in range(1, len(positions)):
            if tau(positions[idx], positions[min_idx]) < 0:
                min_idx = idx
        positions[min_idx], positions[-1] = positions[-1], positions[min_idx]
        tau_sorted.append(positions.pop())

    # Selection sort tau_sorted by descending row (sigma)
    sigma_sorted = []
    while tau_sorted:
        max_idx = 0
        for idx in range(1, len(tau_sorted)):
            if sigma(tau_sorted[idx], tau_sorted[max_idx]) < 0:
                max_idx = idx
        tau_sorted[max_idx], tau_sorted[-1] = tau_sorted[-1], tau_sorted[max_idx]
        sigma_sorted.append(tau_sorted.pop())

    return sigma_sorted