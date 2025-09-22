def main():
    # Input
    n = int(input())
    
    # Initialize Boolean Array
    b = [True] * n
    
    # Initialize Counters
    j = 0
    i = 1
    
    # Loop Until Limit
    while i <= 500000:
        # Check Boolean Condition
        if b[j]:
            b[j] = False  # mark index j as processed
        i += 1
        j = (j + i) % n  # calculate the next index in a circular manner
    
    # Filter True Values
    x = [value for value in b if value]
    
    # Output Result
    if len(x) == 0:
        print("YES")
    else:
        print("NO")

# Call main function to run the program
main()
