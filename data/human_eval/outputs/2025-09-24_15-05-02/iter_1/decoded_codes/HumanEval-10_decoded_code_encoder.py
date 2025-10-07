def is_palindrome(s):
    return s == s[::-1]

def make_palindrome(s):
    if s == '':
        return ''
    i = 0
    while not is_palindrome(s[i:]):
        i += 1
    return s + s[:i][::-1]