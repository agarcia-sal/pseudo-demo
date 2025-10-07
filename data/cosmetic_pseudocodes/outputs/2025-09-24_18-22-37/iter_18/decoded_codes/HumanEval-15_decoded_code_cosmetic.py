from typing import List

def string_sequence(zebra_alpha: int) -> str:
    output_result: List[str] = []
    delta_bravo: int = 0
    while delta_bravo <= zebra_alpha:
        epsilon_charlie: str = str(delta_bravo)
        output_result.append(epsilon_charlie)
        delta_bravo += 1
    return " ".join(output_result)