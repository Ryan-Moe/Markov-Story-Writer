# MDict.py
# Ryan Moe
# Contains the table of sub-tables structure that contains the words read
# in from the books.

from random import randrange

class MDict:
    def __init__(self):
        self.prime = dict()

    # Read all words from a given file into the structure
    def readfile(self, filename):
        file = open(filename)
        fstring = file.read()
        file.close()
        fstring = fstring.lower()
        strList = fstring.split()

        listlen = len(strList) - 2
        for i in range(listlen):
            word1 = strList[i]
            word2 = strList[i+1]
            word3 = strList[i+2]

            if word1 not in self.prime:
                self.prime[word1] = dict()
            if word2 not in self.prime[word1]:
                self.prime[word1][word2] = dict()
            if word3 not in self.prime[word1][word2]:
                self.prime[word1][word2][word3] = 1
            else:
                self.prime[word1][word2][word3] += 1

    # Selects the next word given the previous two, in order.
    def nextword(self, word1, word2):
        ndict = self.prime[word1][word2]
        words = ndict.keys()
        next = ""

        total = 0
        for i in ndict:
            total += ndict[i]

        selection = randrange(total)
        for w in words:
            selection -= ndict[w]
            if selection < 0:
                next = w
                break

        return next

    # Selects the first two words of a story, returns them as a tuple.
    def firstwords(self):
        word1 = ""
        word2 = ""

        primekeys = list(self.prime.keys())
        word1 = primekeys[randrange(len(primekeys))]

        seckeys = list(self.prime[word1].keys())
        word2 = seckeys[randrange(len(seckeys))]

        return (word1, word2)

    # Creates a story of the given length
    def story(self, length):
        storystr = ""
        first = self.firstwords()
        a = first[0]
        b = first[1]

        storystr += a + ' ' + b

        for i in range(length - 1):
            c = self.nextword(a, b)
            storystr += ' ' + c
            a = b
            b = c

        return storystr


m = MDict()
output = open("output.txt", "w")

m.readfile('./stories/doyle-27.txt')
m.readfile('./stories/doyle-case-27.txt')
m.readfile('./stories/twain-adventures-27.txt')
m.readfile('./stories/alice-27.txt')
m.readfile('./stories/london-call-27.txt')
m.readfile('./stories/melville-billy-27.txt')
output.write(m.story(1000))
