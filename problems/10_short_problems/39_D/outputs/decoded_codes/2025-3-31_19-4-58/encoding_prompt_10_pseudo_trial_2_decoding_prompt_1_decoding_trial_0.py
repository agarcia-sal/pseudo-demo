def main():
    # Step 1: Input values
    t1 = input()  # Enter first set of values (t1)
    t2 = input()  # Enter second set of values (t2)

    # Step 2: Split input strings into lists
    tt1 = t1.split()  # Split t1 into list of strings
    tt2 = t2.split()  # Split t2 into list of strings

    # Step 3: Compare values
    res = 0  # Initialize result counter
    for x in range(3):  # Iterate from 0 to 2
        # Step 3a: Convert string values to integers
        a = int(tt1[x])  # Convert tt1[x] to integer
        b = int(tt2[x])  # Convert tt2[x] to integer
        
        # Step 3b: Check for inequality
        if a != b:  # Check if a is not equal to b
            res += 1  # Increment res by 1

    # Step 4: Determine result based on inequality count
    if res < 3:  # Check if res is less than 3
        print("YES")
    else:
        print("NO")

# Call the main function to execute
main()
