def doMain():
    # Step 1: Read input
    t1 = input()  # First set of numbers
    t2 = input()  # Second set of numbers
    
    # Step 2: Split the inputs into lists
    tt1 = t1.split()  # Splitting the first input string into a list
    tt2 = t2.split()  # Splitting the second input string into a list
    
    # Step 3: Initialize a counter to track differences
    res = 0  # Counter for differences
    
    # Step 4: Compare elements in both lists
    for x in range(3):  # Loop through the first three elements
        # Convert string elements to integers
        a = int(tt1[x])  # Convert the x-th element of tt1 to integer
        b = int(tt2[x])  # Convert the x-th element of tt2 to integer
        
        # If the elements are not equal, increment the counter
        if a != b:
            res += 1  # Increment the difference counter if they are not equal
    
    # Step 5: Determine and output the result based on the counter
    if res < 3:
        print("YES")  # Fewer than 3 differences
    else:
        print("NO")   # 3 or more differences

# Program Execution Start
doMain()  # Call the function to execute the logic
