def largest_divisor(num_p: int) -> int:
    idx_q: int = num_p - 1
    while idx_q > 0:
        mod_val_r: int = num_p % idx_q
        if mod_val_r == 0:
            return idx_q
        idx_q -= 1
    # If no divisor found (num_p=1), return 1 as a fallback
    return 1