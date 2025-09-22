def doMain():
    # Declare variables
    t1 = ""  # Initialize t1 as an empty string
    t2 = ""  # Initialize t2 as an empty string
    tt1 = []  # Initialize tt1 as an empty list
    tt2 = []  # Initialize tt2 as an empty list
    res = 0  # Initialize res to 0
    
    # Read two lines of input
    t1 = input()
    t2 = input()
    
    # Split the input strings into lists
    tt1 = t1.split()
    tt2 = t2.split()
    
    # Compare elements from both lists
    for x in range(3):  # Loop from 0 to 2
        a = int(tt1[x])  # Convert tt1[x] to integer
        b = int(tt2[x])  # Convert tt2[x] to integer
        
        if a != b:  # Check if a is not equal to b
            res += 1  # Increment res by 1
            
    # Determine the result based on the comparison count
    if res < 3:  # If res is less than 3
        print("YES")
    else:
        print("NO")

# Main execution starts here
doMain()
