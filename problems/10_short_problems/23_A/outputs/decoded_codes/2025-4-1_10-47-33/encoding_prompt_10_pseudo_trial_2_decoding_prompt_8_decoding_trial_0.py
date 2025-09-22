# Read Input
line = input()[:-1]  # Omit the last character
n = len(line)
rv = 0  # This will hold the result

# Loop Through Lengths
for l in range(n):
    for i in range(n):
        # Check for substring occurrence
        if line[i:i + l] in line[i + 1:]:
            rv = l
            break  # Exit the inner loop

# Output Result
print(rv)


def longest_repeating_substring():
    line = input()[:-1]
    n = len(line)
    rv = 0
    
    # Additional code to ensure functionality and debug information could be integrated here

    for l in range(n):
        for i in range(n):
            if line[i:i + l] in line[i + 1:]:
                rv = l
                break

    print(rv)

# Call the function to execute the logic
longest_repeating_substring()
