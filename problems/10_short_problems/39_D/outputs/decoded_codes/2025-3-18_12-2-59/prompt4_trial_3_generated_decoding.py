def main():
    # Read two lines of input
    line1 = input()
    line2 = input()
    
    # Split each input line into a list of strings
    list1 = line1.split()
    list2 = line2.split()
    
    # Initialize discrepancy counter
    mismatch_count = 0 
    
    # Iterate through first three elements of both lists
    for index in range(3):
        # Convert strings to integers
        value1 = int(list1[index])
        value2 = int(list2[index])
        
        # Check if the values are different
        if value1 != value2:
            mismatch_count += 1
            
    # Determine and output the result based on mismatch count
    if mismatch_count < 3:
        print("YES")
    else:
        print("NO")

# Start the program
main()
