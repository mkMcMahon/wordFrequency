import re
import string

frequency = {}
document_text = open('race.txt', encoding='utf-8')
text_string = document_text.read().lower()
str2 = document_text.read()
# breakdown the string into a list of words
words1 = str2.split()
# sort the list
words1.sort()
# display the sorted words

# initialize an empty string
str1 = ""

# traverse in the string adding words
for w in words1:
    str1 += w + " "

match_pattern = re.findall(r'\b[a-z]{3,15}\b', str1)

for word in match_pattern:
    count = frequency.get(word, 0)
    frequency[word] = count + 1

frequency_list = frequency.keys()

for words in frequency_list:
    print(words, frequency[words])
