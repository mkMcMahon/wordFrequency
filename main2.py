def wordSorter():
    raceObject = open('race.txt', encoding='utf-8')
    str = raceObject.read().lower()
    # breakdown the string into a list of words
    words1 = str.split()
    # sort the list
    words1.sort()
    # initialize an empty string
    str1 = ""
    # traverse in the string adding words
    for word in words1:
        word = word.replace('(', '')
        word = word.replace('.', '')
        word = word.replace(',', '')
        word = word.replace('\'', '')
        word = word.replace('”', '')
        word = word.replace(':', '')
        word = word.replace(';', '')
        str1 += word+" "
    counts = dict()
    words = str1.split()
    # print(words)
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    for k, v in counts.items():
        print (k, '-->', v)
wordSorter()