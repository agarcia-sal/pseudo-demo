def triangle_area(xyz_alpha: float, xyz_beta: float) -> float:
    xyz_flag: bool = True
    xyz_temp1: float = xyz_alpha
    xyz_temp2: float = xyz_beta
    xyz_temp3: float = 2.0
    xyz_result: float = 0.0

    while xyz_flag:
        xyz_calc: float = xyz_temp1 * xyz_temp2
        xyz_div: float = xyz_calc / xyz_temp3
        xyz_result = xyz_div
        xyz_flag = False

    return xyz_result