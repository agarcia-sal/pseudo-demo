def reverse_delete(string_s, string_c):
    string_s = ''.join(ch for ch in string_s if ch not in string_c)
    return (string_s, string_s == string_s[::-1])