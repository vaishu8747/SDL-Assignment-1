text = open("sample.txt","r") # open file in read mode

counts = dict()     # create an empty dictionary

for line in text:  # loop through each line of the file
    line = line.strip()  # remove the leading spaces and newline character
    words = line.split(" ")    # splite the line into words

    #iterate over each word in line
    for word in words:
        # check if the word is already in dictionary
        if word in counts:
            # Increament count of word by 1
            counts[word] = counts[word] + 1
        else:
            # add the word to dictionary with count 1
            counts[word] = 1
 # print the content of dictionary
for key in list(counts.keys()):
    print(key, ":", counts[key])