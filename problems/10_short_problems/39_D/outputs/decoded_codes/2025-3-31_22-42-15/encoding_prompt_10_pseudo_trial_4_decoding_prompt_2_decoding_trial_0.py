def doMain():
    # Step 1: Read input values
    t1 = input()
    t2 = input()
    
    # Step 2: Split inputs into lists of strings
    tt1 = t1.split()
    tt2 = t2.split()
    
    # Step 3: Initialize a result counter
    res = 0
    
    # Step 4: Loop to compare elements in both lists
    for index in range(3):  # Loop from 0 to 2
        # Convert string to integer for comparison
        a = int(tt1[index])
        b = int(tt2[index])
        
        # Step 5: Check if the values are different
        if a != b:
            # INCREMENT res by 1
            res += 1
            
    # Step 6: Determine if the result is less than 3
    if res < 3:
        print("YES")
    else:
        print("NO")

# Step 7: Execute the main function
doMain()
