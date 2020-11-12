def wordsorter():
    raceobject = open('race.txt', encoding='utf-8')
    str = raceobject.read().lower()
    raceobject.close()
    # breakdown the string into a list of words
    words1 = str.split()
    # sort the list (saved as list
    words1.sort()
    # initialize an empty string
    str1 = ""
    # traverse in the string adding words
    for word in words1:
        if word.find('.' or '(' or ',' or '\'' or '”' or ':' or ";" or '“'):
            word = word.replace('(', '')
            word = word.replace('.', '')
            word = word.replace(',', '')
            word = word.replace('\'', '')
            word = word.replace('”', '')
            word = word.replace(':', '')
            word = word.replace(';', '')
            word = word.replace('“', '')
            str1 += word+" "
    counts = dict()
    words = str1.split()
    # print(words)
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    #    print(counts)
    for k, v in counts.items():
       print(k, '-->', v)
