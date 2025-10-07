def circular_shift(integer_x: int, integer_shift: int) -> str:
    string_omega = str(integer_x)
    length_omega = len(string_omega)

    if integer_shift > length_omega:
        reversed_omega = ""
        idx_alpha = length_omega - 1
        while idx_alpha >= 0:
            reversed_omega += string_omega[idx_alpha]
            idx_alpha -= 1
        return reversed_omega
    else:
        cutoff_index = length_omega - integer_shift
        part_one = ""
        idx_beta = cutoff_index
        while idx_beta < length_omega:
            part_one += string_omega[idx_beta]
            idx_beta += 1

        part_two = ""
        idx_gamma = 0
        while idx_gamma < cutoff_index:
            part_two += string_omega[idx_gamma]
            idx_gamma += 1

        return part_one + part_two