def wordcount_short(text_file):
    """Prints the number of times each word appears in a file"""


    text = open(text_file)

    word_count = {}

    for line in text:
        line = line.rstrip()
        line = line.split(" ")

        for word in line:

            #Adds first instance of each word to the dictionary with value 1
            if word not in word_count:
                word_count[word] = 1

            #Increases value count for each additional instance of word
            elif word in word_count:
                word_count[word] += 1

    for word, count in word_count.items():
        print word, count

    text.close()


wordcount_short("test.txt")

















# def wordcount_long()