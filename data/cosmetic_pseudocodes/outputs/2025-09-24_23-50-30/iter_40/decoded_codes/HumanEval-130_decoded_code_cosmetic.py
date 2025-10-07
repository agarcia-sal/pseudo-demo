from typing import List

def tri(parameter_a: int) -> List[float]:
    if parameter_a == 0:
        return [1]
    else:
        storage_b: List[float] = [1, 3]
        counter_c: int = 2
        while counter_c <= parameter_a:
            if counter_c % 2 == 0:
                storage_b.append((counter_c / 2) + 1)
            else:
                storage_b.append(storage_b[counter_c - 1] + storage_b[counter_c - 2] + ((counter_c + 3) / 2))
            counter_c += 1
        return storage_b