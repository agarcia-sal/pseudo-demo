def do_main():
    # Declare input variables for the two lines of integers
    t1 = input()
    t2 = input()

    # Split the input strings into lists of strings
    tt1 = t1.split()
    tt2 = t2.split()

    # Initialize result counter
    res = 0
    
    # Compare elements from both lists
    for x in range(3):  # Loop from 0 to 2
        a = int(tt1[x])  # Convert string to integer for first list
        b = int(tt2[x])  # Convert string to integer for second list
        
        if a != b:  # Check if the integers are not equal
            res += 1  # Increment the difference counter

    # Determine the result based on the comparison count
    if res < 3:
        print("YES")
    else:
        print("NO")

# Main execution starts here
do_main()
