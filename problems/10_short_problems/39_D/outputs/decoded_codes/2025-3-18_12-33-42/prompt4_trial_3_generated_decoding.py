def main():
    # Read input values
    t1 = input()
    t2 = input()
    
    # Split input strings into lists of strings
    tt1 = t1.split()
    tt2 = t2.split()
    
    # Initialize a counter for differences
    difference_count = 0 
    
    # Loop through the first three elements of the lists
    for i in range(3):  # Looping through the first three indices (0, 1, 2)
        # Convert string elements to integers
        a = int(tt1[i])
        b = int(tt2[i])
        
        # Check if the integers are different
        if a != b:
            difference_count += 1  # Increment counter if values are not equal
    
    # Determine the output based on the number of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Entry point for the program
if __name__ == "__main__":
    main()
