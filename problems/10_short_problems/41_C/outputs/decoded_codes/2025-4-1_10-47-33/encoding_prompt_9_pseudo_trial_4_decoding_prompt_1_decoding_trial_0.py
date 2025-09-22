# 1. Receive Input:
input_string = input().strip()  # Read a line of input and remove leading/trailing spaces

# 2. Replace Keywords:
modified_string = input_string.replace("dot", ".").replace("at", "@")

# 3. Check Leading Character:
if modified_string.startswith("."):
    modified_string = "dot" + modified_string[1:]  # Prepend "dot" if first char is "."

# 4. Initialize the List and Counter:
counter = 0  # Initialize the counter variable
processed_list = []  # Create an empty list for processed characters

# 5. Check for Leading "at":
if modified_string.startswith("@"):
    modified_string = "at" + modified_string[1:]  # Prepend "at" if it starts with "@"

# 6. Process Each Character:
for char in modified_string:
    if char == "@":
        if counter > 0:
            processed_list.append("at")  # Append "at" if counter > 0
            counter = 1  # Update counter
        else:
            processed_list.append("@")  # Append "@" if it is the first occurrence
            counter = 1  # Update counter
    else:
        processed_list.append(char)  # Append other characters to the list

# 7. Reconstruct the String:
final_string = ''.join(processed_list)  # Join all characters in the list into a single string

# 8. Check for Trailing Character:
if final_string.endswith("."):
    final_string = final_string[:-1] + "dot"  # Replace trailing "." with "dot"

# 9. Output the Result:
print(final_string)  # Print the final processed string
