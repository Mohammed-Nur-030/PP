fname = input("Enter File name: ")
num_lines = 0
num_words = 0
num_chars = 0

with open(fname, 'r') as f:
    for line in f:
        words = line.split()
        num_lines += 1
        num_words += len(words)
        num_chars += len(line)

print("The total number of lines in the given file:", num_lines)
print("The total number of words in the given file:", num_words)
print("The total number of characters in the given file:", num_chars)
