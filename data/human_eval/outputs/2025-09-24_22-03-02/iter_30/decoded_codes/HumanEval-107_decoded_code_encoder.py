def even_odd_palindrome(n):
    def is_palindrome(x):
        string_x = str(x)
        reversed_string_x = ''
        index = len(string_x) - 1
        while index >= 0:
            reversed_string_x += string_x[index]
            index -= 1
        if string_x == reversed_string_x:
            return True
        else:
            return False

    even_palindrome_count = 0
    odd_palindrome_count = 0

    i = 1
    while i <= n:
        if i % 2 == 1:
            if is_palindrome(i):
                odd_palindrome_count += 1
        elif i % 2 == 0:
            if is_palindrome(i):
                even_palindrome_count += 1
        i += 1

    return [even_palindrome_count, odd_palindrome_count]