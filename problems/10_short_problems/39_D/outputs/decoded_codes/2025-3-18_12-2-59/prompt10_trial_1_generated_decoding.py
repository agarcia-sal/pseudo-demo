def do_main():
    # Declare variables
    t1 = input()  # Read first line of numbers
    t2 = input()  # Read second line of numbers
    
    # Split input strings into lists of strings
    tt1 = t1.split()  # Split t1 by spaces
    tt2 = t2.split()  # Split t2 by spaces
    
    # Initialize result counter
    res = 0 
    
    # Loop through the first three elements
    for x in range(3):  # Assuming exactly three elements as per the problem statement
        # Convert string values to integers
        a = int(tt1[x])  
        b = int(tt2[x])  
        
        # Check if the values are different
        if a != b:
            res += 1  # Increment the counter if values differ
            
    # Determine the result based on the number of differences
    if res < 3:
        print("YES")  # Less than 3 differences
    else:
        print("NO")   # 3 or more differences

# Main program execution
do_main()
