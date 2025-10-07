from typing import Union
import math

def triangle_area(alpha_x: float, beta_y: float, gamma_z: float) -> Union[float, int]:
    # Check triangle inequality
    if not ((alpha_x + beta_y > gamma_z) and (alpha_x + gamma_z > beta_y) and (beta_y + gamma_z > alpha_x)):
        return -1  # negative 0x1 is -1 in decimal

    temp_pq: float = (alpha_x + beta_y + gamma_z) / 2  # semi-perimeter

    s1_mn: float = temp_pq - alpha_x
    s2_op: float = temp_pq - beta_y
    s3_qr: float = temp_pq - gamma_z

    mul1_st: float = temp_pq * s1_mn
    mul2_uv: float = mul1_st * s2_op
    result_uv: float = mul2_uv * s3_qr

    sqr_root_xy: float = math.sqrt(result_uv)
    final_wk: float = round(sqr_root_xy, 2)

    return final_wk