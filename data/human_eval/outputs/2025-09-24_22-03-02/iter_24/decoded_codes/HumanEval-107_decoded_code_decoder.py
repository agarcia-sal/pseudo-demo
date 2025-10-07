def even_odd_palindrome(n):
    def is_palindrome(n):
        n_string = str(n)
        reversed_string = ""
        index = len(n_string) - 1
        while index >= 0:
            reversed_string += n_string[index]
            index -= 1
        if n_string == reversed_string:
            return True
        else:
            return False

    even_palindrome_count = 0
    odd_palindrome_count = 0

    i = 1
    while i <= n:
        if (i % 2) == 1 and is_palindrome(i):
            odd_palindrome_count += 1
        elif (i % 2) == 0 and is_palindrome(i):
            even_palindrome_count += 1
        i += 1

    return (even_palindrome_count, odd_palindrome_count)