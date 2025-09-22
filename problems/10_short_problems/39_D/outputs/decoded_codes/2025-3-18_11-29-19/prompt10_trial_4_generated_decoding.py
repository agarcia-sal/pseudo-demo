def do_main():
    # Step 1: Input Prompt
    t1 = input()  # Prompt for the first string input
    t2 = input()  # Prompt for the second string input
    
    # Step 2: Split Inputs
    tt1 = t1.split()  # Split string t1 into a list
    tt2 = t2.split()  # Split string t2 into a list

    # Step 3: Initialize result counter
    res = 0

    # Step 4: Iterate through the first three elements
    for index in range(3):
        # Convert string to integer
        a = int(tt1[index])
        b = int(tt2[index])

        # Check for inequality
        if a != b:
            res += 1  # Increment res by 1 if a and b are not equal

    # Step 5: Determine the result based on the counter
    if res < 3:
        print("YES")  # Print "YES" if less than 3 matches
    else:
        print("NO")  # Print "NO" if 3 or more mismatches

# Main execution starts here
do_main()
