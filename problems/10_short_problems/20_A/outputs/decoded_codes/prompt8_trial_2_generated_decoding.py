import os

# Start Program

# Read Input
file_path = input()

# Normalize File Path
normalized_path = os.path.normpath(file_path)  # Normalize and clean up the path

# Prepare Output
cleaned_path = '/' + '/'.join(part for part in normalized_path.split('/') if part)  # Reduce leading slashes

# Display Result
print(cleaned_path)

# End Program
