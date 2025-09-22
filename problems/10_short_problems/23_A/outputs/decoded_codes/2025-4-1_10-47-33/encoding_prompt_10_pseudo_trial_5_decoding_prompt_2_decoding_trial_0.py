# 1. Import standard input functionality.
import sys

# 2. Read a line of input from standard input and remove the trailing newline character.
line = sys.stdin.read().strip()

# 3. Set variable 'n' to the length of the input line.
n = len(line)

# 4. Initialize variable 'rv' to 0.  // This will hold the result.
rv = 0

# 5. FOR each length 'l' from 0 to n-1 DO:
for l in range(n):
    # 6. FOR each index 'i' from 0 to n-1 DO:
    for i in range(n):
        # 7. Extract the substring from 'line' starting at index 'i' with length 'l'.
        substring = line[i:i+l]
        
        # 8. Check if this substring appears again in 'line' starting from index 'i + 1'.
        if line.find(substring, i + 1) != -1:
            # 9. IF the substring is found THEN:
            # 10. Set 'rv' to the value of 'l'.
            rv = l
            
            # 11. Break out of the inner loop. // Exit the loop for indices 'i' as we found a match.
            break

# 12. Print the value of 'rv'. // Output the result.
print(rv)
