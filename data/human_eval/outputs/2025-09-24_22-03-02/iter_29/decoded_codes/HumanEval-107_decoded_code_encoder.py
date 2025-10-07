def even_odd_palindrome(n):
    def is_palindrome(n):
        string_n = str(n)
        reversed_string_n = ''
        for index in range(len(string_n) - 1, -1, -1):
            reversed_string_n += string_n[index]
        if string_n == reversed_string_n:
            return True
        else:
            return False

    even_palindrome_count = 0
    odd_palindrome_count = 0
    for i in range(1, n + 1):
        if i % 2 == 1 and is_palindrome(i):
            odd_palindrome_count += 1
        elif i % 2 == 0 and is_palindrome(i):
            even_palindrome_count += 1
    return even_palindrome_count, odd_palindrome_count