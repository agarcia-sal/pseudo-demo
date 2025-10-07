def encode_cyclic(input_string: str) -> str:
    group_count = (len(input_string) + 2) // 3
    group_list = [input_string[3*i : min(3*i+3, len(input_string))] for i in range(group_count)]
    for i, group in enumerate(group_list):
        if len(group) == 3:
            group_list[i] = group[1:] + group[0]
    return ''.join(group_list)

def decode_cyclic(input_string: str) -> str:
    return encode_cyclic(encode_cyclic(input_string))