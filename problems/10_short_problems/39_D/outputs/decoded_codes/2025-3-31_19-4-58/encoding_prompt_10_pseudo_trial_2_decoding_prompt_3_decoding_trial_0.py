def main():
    # Declare and initialize variables
    t1 = ""
    t2 = ""
    res = 0
    
    # Step 1: Input values
    t1 = input()  # Enter first set of values (t1):
    t2 = input()  # Enter second set of values (t2):

    # Step 2: Split input strings into lists
    tt1 = t1.split()  # Split t1 into list of strings
    tt2 = t2.split()  # Split t2 into list of strings
    
    # Step 3: Compare values
    for x in range(3):  # Loop over indices 0 to 2
        a = int(tt1[x])  # Convert string values to integers
        b = int(tt2[x])  # Convert string values to integers
        
        # Step 3b: Check for inequality
        if a != b:
            res += 1  # Increment count of differences
    
    # Step 4: Determine result based on inequality count
    if res < 3:
        print("YES")
    else:
        print("NO")

# Calling the main function to execute the program
if __name__ == "__main__":
    main()
