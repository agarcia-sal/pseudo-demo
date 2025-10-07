from typing import List


def tri(parameter_x: int) -> List[int]:
    aggregate_y: List[int] = [1]
    if parameter_x != 0:
        aggregate_y = [1, 3]
        idx_z = 2
        while idx_z <= parameter_x:
            if idx_z % 2 == 0:
                aggregate_y.append((idx_z // 2) + 1)
            else:
                aggregate_y.append(
                    aggregate_y[idx_z - 1]
                    + aggregate_y[idx_z - 2]
                    + ((idx_z + 3) // 2)
                )
            idx_z += 1
    return aggregate_y