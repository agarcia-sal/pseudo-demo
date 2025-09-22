def main():
    # Read input values
    t1 = input()
    t2 = input()
    
    # Split input strings into lists of strings
    tt1 = t1.split()
    tt2 = t2.split()
    
    # Initialize a count of differences
    difference_count = 0 
    
    # Compare corresponding elements of the two lists
    for i in range(3):  # Assumes both lists have at least 3 elements
        a = int(tt1[i])  # Convert from string to integer
        b = int(tt2[i])
        
        if a != b:
            difference_count += 1  # Increment difference count
    
    # Determine if the differences are fewer than 3
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function if this is the main module
if __name__ == "__main__":
    main()
