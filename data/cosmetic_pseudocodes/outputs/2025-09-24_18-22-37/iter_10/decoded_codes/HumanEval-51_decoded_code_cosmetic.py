def remove_vowels(parameter_qx: str) -> str:
    counter_z: int = 0
    result_rv: str = ""
    length_ty: int = len(parameter_qx)

    while counter_z < length_ty:
        current_hk: str = parameter_qx[counter_z]
        current_lower_fx: str = current_hk.lower()

        if current_lower_fx == "a":
            counter_z += 1
            continue
        if current_lower_fx == "e":
            counter_z += 1
            continue
        if current_lower_fx == "i":
            counter_z += 1
            continue
        if current_lower_fx == "o":
            counter_z += 1
            continue
        if current_lower_fx == "u":
            counter_z += 1
            continue

        result_rv += current_hk
        counter_z += 1

    return result_rv