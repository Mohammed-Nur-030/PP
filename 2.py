input_string = "Python is a high-level, general-purpose programming language for webdev and AI."
print("The input string is:", input_string)

mySet = set(input_string) 
print("mySet",mySet)
for element in mySet:
    countOfChar = 0
    for character in input_string:
        if character == element:
            countOfChar += 1
    print("Count of character '{}' is {}".format(element, countOfChar))


