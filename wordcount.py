# put your code here.

def wordcount_short(text_file):
    text = open(text_file)

    all_lists = []
    word_count = {}

    for line in text:
        line = line.rstrip()
        line = line.split(" ")
        # print all_lines
        all_lists.append(line)
    print all_lists

    #word_count = {"seven": 4, "Kits": 1, "sack": 1}
    #key = word
    #value = number of times

        # word_count["seven"] = 1
        # word_count["seven"] = value + 1
        # word_count[word] = count

    #1. add each key once to word_count, and assign value to 1
    for line in all_lists:
        for word in line:
            word_count[word] = 1
    return word_count
  
    #2. loop through text_file

    #3. return key, value

print wordcount_short("test.txt")

















# def wordcount_long()