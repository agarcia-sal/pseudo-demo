def main():
    # Step 1: Input values
    t1 = input()
    t2 = input()

    # Step 2: Split input strings into lists
    tt1 = t1.split()  # Split t1 into list of strings
    tt2 = t2.split()  # Split t2 into list of strings
    
    # Step 3: Compare values
    res = 0  # Initialize result counter
    
    for x in range(3):  # Loop from 0 to 2
        # Step 3a: Convert string values to integers
        a = int(tt1[x])
        b = int(tt2[x])
        
        # Step 3b: Check for inequality
        if a != b:
            res += 1  # Increment res by 1 if values are not equal

    # Step 4: Determine result based on inequality count
    if res < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function
main()
