from typing import Sequence

def has_close_elements(collection_of_values: Sequence[float], limit_value: float) -> bool:
    def check_pairs(position_primary: int) -> bool:
        if position_primary == len(collection_of_values):
            return False

        def examine_secondary(position_secondary: int) -> bool:
            if position_secondary == len(collection_of_values):
                return check_pairs(position_primary + 1)
            if position_primary != position_secondary:
                gap = abs(collection_of_values[position_primary] - collection_of_values[position_secondary])
                if gap < limit_value:
                    return True
            return examine_secondary(position_secondary + 1)

        return examine_secondary(0)

    return check_pairs(0)