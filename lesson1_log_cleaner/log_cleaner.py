import sys

def clean_log(input_file, output_file, banned_keywords):
    cleaned_lines =[]

    with open(input_file, 'r') as f:
        for line in f:
            if not any(keyword in line for keyword in banned_keywords):
                    cleaned_lines.append(line.strip())

    with open(output_file, 'w') as f:
        for line in cleaned_lines:
            f.write(line + '\n')

    print(f"Cleaned log saved to {output_file}")
    print(f"Kept {len(cleaned_lines)} lines")

if __name__ == "__main__":
    banned = ["ERROR", "DEBUG"]
    clean_log("fake_log.txt", "cleaned.log.txt", banned)

    if len(sys.argv) < 4:
        print("Usage: python log_cleaner.py input_file output_file keyword1 keyrowd2")
        print("Example: python log_cleaner.py fake_log.txt cleaned.txt ERROR DEBUG")

        sys.exit(1)

    # grab filenames from args
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    banned_keywords = sys.argv[3:] # [3:0] -> arguments from index to the last


    # validating inputs

    if not(input_file.endswith(".txt") or input_file.endswith(".txt")):
        print(f"{input_file} is not a valid input file")
        sys.exit(1)

    if not (output_file.endswith(".txt") or output_file.endswith(".log")):
        print(f"{output_file} is not a valid output file.")
        sys.exit(1)

    print(f"Input file: {input_file}")
    print(f"Output file: {output_file}")
    print(f"Filtering out: {banned_keywords}")


    #call clean_log and pass in args
    clean_log(input_file, output_file, banned_keywords)




# the purpose of this py script is to create a text file with cleaned logs by filtering out banned keywords such as "ERROR" and "DEBUG". Users can provide their own keywords that they want filtered out. Input arguments will be validated

# learned concepts:
# 1. general comprehesion - similar to list comprehesion 
# >>> if not any(keyword in line for keyword in banned_keywords):

# 2. opening files in r or w mode 
# 3. sys.argv - system argument vector ; python slips args by spaces