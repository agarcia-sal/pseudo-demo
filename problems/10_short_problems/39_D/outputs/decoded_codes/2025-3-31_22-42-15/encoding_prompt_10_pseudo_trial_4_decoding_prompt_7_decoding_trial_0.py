def doMain():
    # Step 1: Read input values
    t1 = input()  # Read the first line of input
    t2 = input()  # Read the second line of input
    
    # Step 2: Split inputs into lists of strings
    tt1 = t1.split()  # Split first input into a list of strings
    tt2 = t2.split()  # Split second input into a list of strings
    
    # Step 3: Initialize a result counter
    res = 0  # Counter for the number of differences
    
    # Step 4: Loop to compare elements in both lists
    for index in range(3):  # Loop through indices 0 to 2
        # Convert string to integer for comparison
        a = int(tt1[index])  # Convert the string from list 1 to integer
        b = int(tt2[index])  # Convert the string from list 2 to integer
        
        # Step 5: Check if the values are different
        if a != b:  # Compare the two integers
            res += 1  # Increment the counter if they are not equal
            
    # Step 6: Determine if the result is less than 3
    if res < 3:  # Check the count of differences
        print("YES")  # Print "YES" if differences are less than 3
    else:
        print("NO")  # Print "NO" if differences are 3 or more

# Step 7: Execute the main function
doMain()
