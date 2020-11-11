
raceObject = open('race.txt', encoding='utf-8')
str = raceObject.read()
# breakdown the string into a list of words
words1 = str.split()
# sort the list
words1.sort()
# display the sorted words

# initialize an empty string
str1 = ""

# traverse in the string adding words
for word in words1:
    if word.__contains__('(' or '.' or ','):
        word = word.replace('(', '')
        word = word.replace('.', '')
        word = word.replace(',', '')
    word = word.replace('(', '')
    word = word.replace('.', '')
    word = word.replace(',', '')
    word = word.replace('\'', '')
    word = word.replace('\"', '')
    str1 += word+" "

def word_count(str):
    counts = dict()
    words = str.split()
    #print(words)
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts


print( word_count(str1))
