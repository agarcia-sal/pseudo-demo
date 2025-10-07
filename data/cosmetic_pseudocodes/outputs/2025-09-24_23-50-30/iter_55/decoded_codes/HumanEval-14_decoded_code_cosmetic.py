from typing import List

def all_prefixes(parameter_alpha: str) -> List[str]:
    container_beta: List[str] = []

    def gamma(delta: int, epsilon: int):
        if delta >= epsilon:
            return
        yield parameter_alpha[:delta + 1]
        yield from gamma(delta + 1, epsilon)

    # Consume the generator to populate container_beta
    for element_zeta in gamma(0, len(parameter_alpha)):
        container_beta.append(element_zeta)
    return container_beta