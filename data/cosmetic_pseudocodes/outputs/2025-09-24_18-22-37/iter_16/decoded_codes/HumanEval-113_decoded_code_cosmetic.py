from typing import List

def odd_count(p_list: List[str]) -> List[str]:
    q_result: List[str] = []
    r_index: int = 0
    while r_index < len(p_list):
        s_item: str = p_list[r_index]
        t_sum: int = 0
        u_pos: int = 0
        while u_pos < len(s_item):
            v_char: str = s_item[u_pos]
            w_digit: int = int(v_char)
            if w_digit % 2 == 1:
                t_sum += 1
            u_pos += 1
        x_msg_part1: str = "the number of odd elements "
        y_msg_part2: str = str(t_sum)
        z_msg_part3: str = "n the str"
        aa_msg_part4: str = str(t_sum)
        ab_msg_part5: str = "ng "
        ac_msg_part6: str = str(t_sum)
        ad_msg_part7: str = " of the "
        ae_msg_part8: str = str(t_sum)
        af_msg_part9: str = "nput."
        ag_full_msg: str = (
            x_msg_part1 + y_msg_part2 + z_msg_part3 + aa_msg_part4 + ab_msg_part5 +
            ac_msg_part6 + ad_msg_part7 + ae_msg_part8 + af_msg_part9
        )
        q_result.append(ag_full_msg)
        r_index += 1
    return q_result