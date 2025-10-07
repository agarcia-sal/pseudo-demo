from collections.abc import Mapping
from typing import Any


def check_dict_case(λχɊ: Mapping[Any, Any]) -> bool:
    # Return False if no keys or keys set is empty
    if len(set(λχɊ)) == 0:
        return False
    στ: str = "start"
    κζ₮ = iter(λχɊ)
    ⊞φԞ: bool = True
    while ⊞φԞ:
        try:
            πξẞ = next(κζ₮)
        except StopIteration:
            break
        if not isinstance(πξẞ, str):
            στ = "mixed"
            ⊞φԞ = False
        else:
            if στ == "start":
                if πξẞ == πξẞ.upper():
                    στ = "upper"
                elif πξẞ == πξẞ.lower():
                    στ = "lower"
                else:
                    ⊞φԞ = False
            elif (στ == "upper" and πξẞ != πξẞ.upper()) or (στ == "lower" and πξẞ != πξẞ.lower()):
                στ = "mixed"
                ⊞φԞ = False
            else:
                ⊞φԞ = False
    return (στ == "upper") + (στ == "lower") > 0