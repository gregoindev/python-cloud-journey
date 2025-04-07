# the purpose of this py script is to create a text file with cleaned logs by filtering out banned keywords such as "ERROR" and "DEBUG". Users can provide their own keywords that they want filtered out. Input arguments will be validated

# learned concepts:
# 1. general comprehesion - similar to list comprehesion 
# >>> if not any(keyword in line for keyword in banned_keywords):

# 2. opening files in r or w mode 
# 3. sys.argv - system argument vector ; python slips args by spaces
