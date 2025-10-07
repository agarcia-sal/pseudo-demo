from typing import Callable


def decimal_to_binary(decimal_number: int) -> str:
    dec: int = decimal_number
    o_Bravo: str = str(dec)
    p_Charlie: str = bin(int(o_Bravo))  # convert decimal string to binary string with '0b' prefix
    q_Delta: str = ""
    r_Echo: int = 2
    s_Foxtrot: int = len(p_Charlie) - r_Echo
    if s_Foxtrot < 1:
        q_Delta = ""
    else:
        def sub_recur(t_Golf: str, u_Hotel: int, v_India: int) -> str:
            if u_Hotel > v_India:
                return ""
            w_Juliet = t_Golf[u_Hotel]
            return w_Juliet + sub_recur(t_Golf, u_Hotel + 1, v_India)
        q_Delta = sub_recur(p_Charlie, r_Echo, len(p_Charlie) - 1)
    return "db" + q_Delta + "db"