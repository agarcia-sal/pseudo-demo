def do_main():
    # Read two lines of input
    t1 = input()
    t2 = input()
    
    # Split the input strings into lists
    tt1 = t1.split()
    tt2 = t2.split()
    
    # Initialize a counter for differences
    res = 0 

    # Iterate through the first three elements of the lists
    for x in range(3):
        # Convert elements to integers for comparison
        a = int(tt1[x])
        b = int(tt2[x])
        
        # Increment the difference counter if the elements are not equal
        if a != b:
            res += 1 

    # Check the number of differences found
    if res < 3:
        print("YES")
    else:
        print("NO")

# Main entry point for the program
if __name__ == "__main__":
    do_main()
