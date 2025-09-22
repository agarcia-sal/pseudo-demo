def doMain():
    # Step 1: Get input from the user
    t1 = input()
    t2 = input()
    
    # Step 2: Split input strings into lists
    tt1 = t1.split()  # Split by whitespace
    tt2 = t2.split()  # Split by whitespace
    
    # Step 3: Initialize a counter for differences
    res = 0 
    
    # Step 4: Compare corresponding elements from both lists
    for x in range(3):  # Loop from 0 to 2
        a = int(tt1[x])  # Convert to integer
        b = int(tt2[x])  # Convert to integer
        
        # Check if the elements are different
        if a != b:  # If not equal
            res += 1  # Increment the difference counter
    
    # Step 5: Determine the outcome based on the number of differences
    if res < 3:
        print("YES")  # Less than 3 differences
    else:
        print("NO")   # 3 or more differences

# Main execution
doMain()
