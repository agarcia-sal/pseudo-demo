def main():
    # Step 1: Input values
    t1 = input()  # User input for the first set of values
    t2 = input()  # User input for the second set of values

    # Step 2: Split input strings into lists
    tt1 = t1.split()  # Split t1 into list of strings
    tt2 = t2.split()  # Split t2 into list of strings
    
    res = 0  # Initialize a counter for inequalities

    # Step 3: Compare values
    for x in range(3):  # Loop from 0 to 2 (inclusive)
        # Step 3a: Convert string values to integers
        a = int(tt1[x])  # Convert the value from the first list
        b = int(tt2[x])  # Convert the value from the second list
        
        # Step 3b: Check for inequality
        if a != b:
            res += 1  # Increment counter if values are not equal

    # Step 4: Determine result based on inequality count
    if res < 3:
        print("YES")  # Print YES if fewer than 3 are unequal
    else:
        print("NO")   # Print NO if 3 or more are unequal

# Entry point of the program
if __name__ == "__main__":
    main()
