import sys

#check if sys.argv is valid length is enough

if len(sys.argv) != 4:
    print("Format: python log_search.py input_file output_file keyword")
    sys.exit(1)

# assign CLI args to variables
input_file = sys.argv[1]
output_file = sys.argv[2]
keyword = sys.argv[3]

matches = []

with open(input_file, 'r') as f:
    for line in f:
        if keyword.lower() in line.lower():
            matches.append(line.strip())


with open(output_file, 'w') as f:
    for line in matches:
        f.write(line + '\n')

print(f"Found {len(matches)} lines containing '{keyword}")
print(f"Results written to {output_file}")




