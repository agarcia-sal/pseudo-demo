# Main Procedure
def main():
    # Step 1: Input values
    t1 = input()  # Read first set of values
    t2 = input()  # Read second set of values

    # Step 2: Split input strings into lists
    tt1 = t1.split()  # Split t1 into list of strings
    tt2 = t2.split()  # Split t2 into list of strings
    
    # Initialize result counter
    res = 0  # Number of differing values

    # Step 3: Compare values
    for x in range(3):  # Loop from 0 to 2 (three values)
        # Step 3a: Convert string values to integers
        a = int(tt1[x])  # Convert value from tt1 to integer
        b = int(tt2[x])  # Convert value from tt2 to integer
        
        # Step 3b: Check for inequality
        if a != b:  # If values are not equal
            res += 1  # Increment the counter

    # Step 4: Determine result based on inequality count
    if res < 3:  # If less than 3 values are different
        print("YES")  # Output YES
    else:
        print("NO")  # Output NO

# Call the main function to execute the procedure
main()
