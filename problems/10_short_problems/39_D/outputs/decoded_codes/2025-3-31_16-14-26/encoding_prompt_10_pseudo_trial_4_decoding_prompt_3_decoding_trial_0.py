def doMain():
    # Step 1: Read input
    t1 = input()
    t2 = input()
    
    # Step 2: Split the inputs into lists
    tt1 = t1.split()
    tt2 = t2.split()
    
    # Step 3: Initialize a counter to track differences
    res = 0
    
    # Step 4: Compare elements in both lists
    for x in range(3):
        # Convert string elements to integers
        a = int(tt1[x])
        b = int(tt2[x])
        
        # If the elements are not equal, increment the counter
        if a != b:
            res += 1
            
    # Step 5: Determine and output the result based on the counter
    if res < 3:
        print("YES")
    else:
        print("NO")

# Program Execution Start
doMain()
