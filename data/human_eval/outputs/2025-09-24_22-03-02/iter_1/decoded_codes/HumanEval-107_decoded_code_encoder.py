def is_palindrome(x):
    s = str(x)
    return s == s[::-1]

def count_palindromes(n):
    even_count, odd_count = 0, 0
    for i in range(1, n+1):
        if is_palindrome(i):
            if i % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
    return even_count, odd_count