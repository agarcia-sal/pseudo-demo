def doMain():
    # Step 1: Get input from the user
    t1 = input()  # First input string
    t2 = input()  # Second input string
    
    # Step 2: Split input strings into lists
    tt1 = t1.split()  # Split the first input string by whitespace
    tt2 = t2.split()  # Split the second input string by whitespace
    
    # Step 3: Initialize a counter for differences
    res = 0  # Initialize the difference counter
    
    # Step 4: Compare corresponding elements from both lists
    for x in range(3):  # We compare the first three elements
        a = int(tt1[x])  # Convert the xth element of tt1 to integer
        b = int(tt2[x])  # Convert the xth element of tt2 to integer
        
        # Check if the elements are different
        if a != b:  # If the elements are different
            res += 1  # Increment the difference counter
    
    # Step 5: Determine the outcome based on the number of differences
    if res < 3:  # If there are less than 3 differences
        print("YES")  # Output "YES"
    else:  # If there are 3 or more differences
        print("NO")   # Output "NO"

# Main execution
doMain()
