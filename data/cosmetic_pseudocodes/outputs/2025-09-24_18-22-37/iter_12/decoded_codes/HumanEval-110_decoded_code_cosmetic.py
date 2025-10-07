from typing import List

def exchange(list_one: List[int], list_two: List[int]) -> str:
    counter_alpha: int = 0
    counter_beta: int = 0
    index_x: int = 0
    while index_x < len(list_one):
        temp_val: int = list_one[index_x]
        mod_res: int = temp_val - 2 * (temp_val // 2)  # modulus without %
        if mod_res != 0:
            counter_alpha += 1
        index_x += 1
    for idx_beta in range(len(list_two)):
        val_beta: int = list_two[idx_beta]
        rem_beta: int = val_beta - 2 * (val_beta // 2)
        if rem_beta == 0:
            counter_beta += 1
    if counter_beta >= counter_alpha:
        return "YES"
    else:
        return "NO"