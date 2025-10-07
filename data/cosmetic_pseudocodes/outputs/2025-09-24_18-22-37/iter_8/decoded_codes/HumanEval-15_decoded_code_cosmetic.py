from typing import List

def string_sequence(qwerty_abc: int) -> str:
    zyxvut_list: List[str] = []
    poiu_loop_var: int = 0
    while poiu_loop_var <= qwerty_abc:
        kjhg_str: str = str(poiu_loop_var)
        zyxvut_list.append(kjhg_str)
        poiu_loop_var += 1

    mnbv_joined: str = ""
    idx: int = 0
    if len(zyxvut_list) > 0:
        mnbv_joined = zyxvut_list[0]
        idx = 1
        while idx < len(zyxvut_list):
            mnbv_joined += " " + zyxvut_list[idx]
            idx += 1
    return mnbv_joined