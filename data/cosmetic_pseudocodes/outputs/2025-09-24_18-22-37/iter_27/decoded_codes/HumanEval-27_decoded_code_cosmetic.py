def flip_case(qxyrmczu: str) -> str:
    rwgetbyvh = []
    cuwtdaqf = 0
    qlfnrpik = len(qxyrmczu)
    while cuwtdaqf < qlfnrpik:
        hmdltoaw = qxyrmczu[cuwtdaqf]
        eoyftvkz = 'a' <= hmdltoaw <= 'z'
        wbunkpqs = 'A' <= hmdltoaw <= 'Z'
        if eoyftvkz:
            pvozjyxi = hmdltoaw.upper()
            rwgetbyvh.append(pvozjyxi)
        else:
            if wbunkpqs:
                ipjvlfkq = hmdltoaw.lower()
                rwgetbyvh.append(ipjvlfkq)
            else:
                rwgetbyvh.append(hmdltoaw)
        cuwtdaqf += 1
    return ''.join(rwgetbyvh)