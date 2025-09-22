# Define the main program logic
def main():
    # Read input string from standard input
    s = input()
    i = 0  # Initialize index
    ans = ""  # Initialize output string

    # Loop through each character of the string 's'
    while i < len(s):
        # Check for a single dot
        if s[i] == '.':
            ans += '0'  # Append '0' for a single dot
            i += 1  # Increment index by 1
        else:
            # Check next character for a dot
            if i + 1 < len(s) and s[i + 1] == '.':
                ans += '1'  # Append '1' for two consecutive dots
                i += 2  # Increment index by 2
            else:
                ans += '2'  # Append '2' for other cases
                i += 2  # Increment index by 2
                
    # Output the final result
    print(ans)

# Execute the main function
if __name__ == "__main__":
    main()
