def do_main():
    # Read two lines of input
    t1 = input()
    t2 = input()
    
    # Split input lines into lists of strings
    tt1 = t1.split()
    tt2 = t2.split()
    
    # Initialize the counter for differing elements
    differences = 0
    
    # Iterate over indices 0 to 2 inclusive
    for index in range(3):
        # Convert string elements to integers
        a = int(tt1[index])
        b = int(tt2[index])
        
        # Increment differences if values are not equal
        if a != b:
            differences += 1
    
    # Output result based on the number of differences
    if differences < 3:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    do_main()
