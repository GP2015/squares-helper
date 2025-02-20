# ------- User defined parameters -------

# Letters in square matrix
sq = ["abcd", "efgh", "ijkl", "mnop"]

# Length of longest word
max = 16

# Lowest frequency to print words of
freqlower = 1.3

# Highest frequency to print words of
frequpper = 2.7

# ---------------------------------------

from wordfreq import zipf_frequency
from urllib.request import urlopen

words = []

inds = []
word = ""

txt = open("output.txt", "w")
print("Opened text file")

def it():
    global inds, word, sq, txt
    for c in range(-1, 2, 1):
        newc = inds[-1][0] + c
        if newc not in (-1, 4):
            for r in range(-1, 2, 1):
                newr = inds[-1][1] + r
                if newr not in (-1, 4) and [newc, newr] not in inds:
                    inds.append([newc, newr])
                    word += sq[newc][newr]
                    if len(word) > 3:
                        freq = zipf_frequency(word, "en")
                        if freq >= freqlower and freq < frequpper and word not in words:
                            url = "https://wordfinder.yourdictionary.com/letter-words/"
                            url += str(len(word)) + "-starts-" + word
                            url += "/?dictionary=WWF"
                            try:
                                urlopen(url)
                                words.append(word)
                            except: 
                                pass
                    if len(word) <= max:
                        it()
                    inds.pop()
                    word = word[:-1]

for c in range(4):
    for r in range(4):
        print("Letter " + str(c * 4 + r + 1) + " of 16")
        inds.append([c, r])
        word += sq[c][r]
        it()
        inds.pop()
        word = word[:-1]
        
for i in words:
    txt.write(i + '\n')

txt.close()
print("Program ended")