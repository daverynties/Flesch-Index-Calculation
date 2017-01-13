import string
import datetime
import matplotlib.pyplot as plt

numLines = 0
numWords = 0
numSentences = 0

numVowels = 0
vowels = 'aeiouy'
listNumSyllables = []
wordList = []

filename = '/Users/dave/CIS/678/P1/ga.txt'

def calc_num_syllables(word):

    silent = None
    num_syllables = 0

    if word.endswith('e'):
        silent = True

    for index, letter in enumerate(word):
        if index == 0 and word[index] in vowels:
            num_syllables += 1
        elif word[index - 1] not in vowels:
            if index < len(word) - 1 and word[index] in vowels:
                num_syllables += 1
            elif index == len(word) - 1 and word[index] in vowels:
                num_syllables += 1

    if num_syllables > 1 and silent:
        num_syllables -= 1

    return num_syllables


with open(filename, 'r') as file:
    for line in file:
        line.replace("...", " ")
        numSentences += line.count('.')
        line = line.translate(None, string.punctuation)
        start_time = datetime.datetime.now()
        for word in line.split():
            listNumSyllables.append(calc_num_syllables(word))
        total_time = datetime.datetime.now() - start_time
        millis = int(total_time.total_seconds() * 1000)

totalSyllables = sum(listNumSyllables)
totalWords = len(listNumSyllables)

aws = totalWords / float(numSentences)
asl = totalSyllables / float(totalWords)

fi = 206.835 - (1.015 * aws) - (84.6 * asl)

print('\nAll Items for Histogram in: listNumSyllables')
print('Number of Sentences: %i' % numSentences)
print('Number of Words: %i' % len(listNumSyllables))
print('Number of Syllables: %i' % (sum(listNumSyllables)))
print('Syllable Count Time: %s Seconds' % total_time)
print('Syllable Count Time: %i Milliseconds' % millis)
print('\nFlesch Index: %.2f' % fi)

plt.hist(listNumSyllables)
plt.title("Syllable Complexity")
plt.xlabel("Number of Syllables")
plt.ylabel("Frequency")
plt.savefig('histogram.png')

