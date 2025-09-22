def main():
    # Step 1: Input values
    t1 = input()  # Read first set of values
    t2 = input()  # Read second set of values

    # Step 2: Split input strings into lists
    tt1 = t1.split()  # Split t1 into list of strings
    tt2 = t2.split()  # Split t2 into list of strings

    # Declare variable to count the number of inequalities
    res = 0

    # Step 3: Compare values
    for x in range(3):  # Loop over the first three elements
        # Step 3a: Convert string values to integers
        a = int(tt1[x])  # Convert tt1[x] to integer
        b = int(tt2[x])  # Convert tt2[x] to integer
        
        # Step 3b: Check for inequality
        if a != b:  # If values are not equal
            res += 1  # Increment the inequality counter

    # Step 4: Determine result based on inequality count
    if res < 3:  # If less than three inequalities
        print("YES")
    else:  # If three or more inequalities
        print("NO")

# Call the main function to execute the program
main()
