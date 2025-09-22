def do_main():
    # Step 1: Get inputs from the user
    t1 = input()
    t2 = input()
    
    # Step 2: Split the input strings into lists of strings
    tt1 = t1.split()
    tt2 = t2.split()
    
    # Step 3: Initialize a result counter
    res = 0
    
    # Step 4: Loop through the first three elements of both lists
    for x in range(3):
        # Convert the string values to integers
        a = int(tt1[x])
        b = int(tt2[x])
        
        # Step 5: Compare the integers
        if a != b:
            # Increment result counter if the values are not equal
            res += 1
            
    # Step 6: Check the result counter
    if res < 3:
        print("YES")
    else:
        print("NO")

# Main program execution
do_main()
