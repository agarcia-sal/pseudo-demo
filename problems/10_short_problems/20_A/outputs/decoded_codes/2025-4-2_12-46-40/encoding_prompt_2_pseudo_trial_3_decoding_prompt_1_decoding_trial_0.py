# 1. Input: Read a string from the standard input
path = input().strip()  # Read input and remove any extra spaces

# 2. Process: Normalize the path
# Normalize the path to address different formatting
normalized_path = path  # Additional normalization can be added as needed

# 3. Identify and replace leading slashes
while normalized_path.startswith('//'):  # Checks for multiple leading slashes
    normalized_path = normalized_path[1:]  # Remove one leading slash

if normalized_path.startswith('/') == False:  # If there's no leading slash
    normalized_path = '/' + normalized_path  # Add a single leading slash

# 4. Output: Display the modified path
print(normalized_path)  # Print cleaned-up path to console
