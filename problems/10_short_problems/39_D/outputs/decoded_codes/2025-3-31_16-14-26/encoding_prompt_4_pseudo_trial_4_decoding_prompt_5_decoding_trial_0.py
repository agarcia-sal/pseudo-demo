def main():
    # Read two lines of input
    t1 = input()
    t2 = input()

    # Split the input strings into lists of strings
    tt1 = t1.split()  # Split by spaces
    tt2 = t2.split()  # Split by spaces
    
    # Initialize a counter for differences
    difference_count = 0 
    
    # Compare corresponding elements of the two lists
    for index in range(3):  # Loop through first three indices
        a = int(tt1[index])  # Convert string to integer
        b = int(tt2[index])  # Convert string to integer
        
        # Count how many elements are different
        if a != b:  # Check for inequality
            difference_count += 1  # Increment counter

    # Determine if differences are less than 3
    if difference_count < 3:
        print("YES")  # Print result if differences are less than 3
    else:
        print("NO")   # Print result if differences are 3 or more

# Main execution starts here
main()
