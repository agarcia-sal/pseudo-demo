from typing import Any, Dict


def check_dict_case(beta: Dict[Any, Any]) -> bool:
    if len(beta.keys()) != 0:
        gamma: str = "start"
        delta: int = 0
        keys = list(beta.keys())
        while delta < len(keys):
            epsilon = keys[delta]
            if not isinstance(epsilon, str):
                gamma = "mixed"
                break
            if gamma == "start":
                if epsilon.isupper():
                    gamma = "upper"
                else:
                    if epsilon.islower():
                        gamma = "lower"
                    else:
                        break
            elif gamma == "upper":
                if not epsilon.isupper():
                    gamma = "mixed"
                    break
                else:
                    break
            elif gamma == "lower":
                if not epsilon.islower():
                    gamma = "mixed"
                    break
                else:
                    break
            delta += 1
        return gamma == "upper" or gamma == "lower"
    else:
        return False