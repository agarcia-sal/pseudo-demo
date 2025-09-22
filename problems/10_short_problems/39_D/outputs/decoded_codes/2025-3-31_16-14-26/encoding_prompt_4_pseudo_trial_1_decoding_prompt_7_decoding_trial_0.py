def main():
    # Read input values from the user
    t1 = input()  # First string input
    t2 = input()  # Second string input
    
    # Split input strings into lists of strings
    tt1 = t1.split()  # Split first input into words
    tt2 = t2.split()  # Split second input into words
    
    # Initialize a count of differences
    difference_count = 0 
    
    # Compare corresponding elements of the two lists
    for i in range(3):  # Assuming we compare the first three elements
        a = int(tt1[i])  # Convert string to integer for the first list
        b = int(tt2[i])  # Convert string to integer for the second list
        
        if a != b:  # Check if the two integers are not equal
            difference_count += 1  # Increment the difference count if they are not equal
    
    # Determine if there are fewer than 3 differences
    if difference_count < 3:
        print("YES")  # Output "YES" if differences are fewer than 3
    else:
        print("NO")   # Output "NO" if differences are 3 or more

# Execute the main function if this is the main module
if __name__ == "__main__":
    main()
