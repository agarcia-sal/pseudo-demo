def main():
    # Read input string from standard input and strip whitespace from both ends
    s = input().strip()
    
    i = 0  # Initialize index counter to 0
    ans = ""  # Initialize the answer string to empty

    # Loop until i reaches the length of s
    while i < len(s):
        if s[i] == '.':
            ans += '0'  # Append '0' to the answer string
            i += 1  # Move to the next character
        elif i + 1 < len(s) and s[i + 1] == '.':
            ans += '1'  # Append '1' to the answer string
            i += 2  # Move to the character after next
        else:
            ans += '2'  # Append '2' to the answer string
            i += 2  # Move to the character after next

    print(ans)  # Output the final answer string

# Execute the main function
if __name__ == "__main__":
    main()
