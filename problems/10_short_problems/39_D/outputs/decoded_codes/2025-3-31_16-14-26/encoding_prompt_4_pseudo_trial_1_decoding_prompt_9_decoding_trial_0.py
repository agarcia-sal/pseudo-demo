def main():
    # Read input values
    t1 = input()
    t2 = input()
    
    # Split input strings into lists of strings
    tt1 = t1.split()
    tt2 = t2.split()
    
    # Initialize a count of differences
    difference_count = 0 
    
    # Ensure we only compare the first three elements if they exist
    for i in range(min(3, len(tt1), len(tt2))):
        # Convert strings to integers
        a = int(tt1[i])
        b = int(tt2[i])
        
        # Increment the count if the integers are not equal
        if a != b:
            difference_count += 1
            
    # Determine if the differences are fewer than 3
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function
if __name__ == "__main__":
    main()
