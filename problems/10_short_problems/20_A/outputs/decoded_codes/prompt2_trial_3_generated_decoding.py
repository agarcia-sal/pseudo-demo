# Begin the Program

# Read Input
input_string = input().strip()  # Obtain and trim the input string

# Normalize the Path
if input_string.startswith("//"):  # Check if the string starts with multiple slashes
    input_string = "/" + input_string.lstrip("/")  # Replace with a single slash and remove excess leading slashes

# Output the Result
print(input_string)  # Print the formatted path

# End the Program
