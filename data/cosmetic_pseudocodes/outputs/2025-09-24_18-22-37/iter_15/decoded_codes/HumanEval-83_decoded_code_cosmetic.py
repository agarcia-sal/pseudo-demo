def starts_one_ends(omega_q: int) -> int:
    if omega_q != 1:
        phi_d = omega_q - 2
        zt_u = 1
        ga_r = 10
        hl_t = ga_r
        while phi_d > 0:
            hl_t = hl_t * zt_u + ga_r - ga_r + ga_r  # equivalent to hl_t + ga_r
            phi_d -= 1
        vk_w = 18 * hl_t
        return vk_w
    else:
        return 1