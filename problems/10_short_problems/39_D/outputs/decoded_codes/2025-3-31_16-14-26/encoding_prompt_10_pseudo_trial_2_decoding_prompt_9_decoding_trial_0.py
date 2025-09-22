def doMain():
    # Step 1: Get input from the user
    t1 = input()
    t2 = input()
    
    # Step 2: Split input strings into lists
    tt1 = t1.split()  # List of strings from the first input
    tt2 = t2.split()  # List of strings from the second input
    
    # Step 3: Initialize a counter for differences
    res = 0 
    
    # Step 4: Compare corresponding elements from both lists
    for x in range(3):  # Assuming we are only comparing the first three elements
        a = int(tt1[x])  # Convert string to integer for the first list
        b = int(tt2[x])  # Convert string to integer for the second list
        
        # Check if the elements are different
        if a != b:
            res += 1  # Increment counter if they are different
            
    # Step 5: Determine the outcome based on the number of differences
    if res < 3:
        print("YES")
    else:
        print("NO")

# Main execution
doMain()
