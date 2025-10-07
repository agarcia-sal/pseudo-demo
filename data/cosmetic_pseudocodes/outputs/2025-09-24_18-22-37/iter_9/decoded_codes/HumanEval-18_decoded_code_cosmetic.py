def how_many_times(phi_string: str, omega_substring: str) -> int:
    xi_total_occurrences: int = 0
    psi_limit: int = len(phi_string) - len(omega_substring)
    alpha_position: int = 0
    while alpha_position <= psi_limit:
        theta_segment: str = phi_string[alpha_position : alpha_position + len(omega_substring)]
        if theta_segment == omega_substring:
            xi_total_occurrences += 1
        alpha_position += 1
    return xi_total_occurrences