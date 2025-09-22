# Read input from standard input and trim leading/trailing whitespace
input_path = input().strip()

# Normalize the file path
# Split the path by slashes, filtering out empty segments
segments = [segment for segment in input_path.split('/') if segment]

# Join the non-empty segments back with a single slash
if segments:
    normalized_path = '/' + '/'.join(segments)
else:
    normalized_path = '/'

# Display the normalized path
print(normalized_path)
