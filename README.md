# Markov-Story-Writer
A python 3 program that uses a Markov chain model to write a story.
This was originally written for a university class.
It writes a "story" of a given length (default 1000 words) the previous two words to randomly choose the next, weighted by a likelihood determined when reading in the given text files. However, because the given files had no punctuation, the story is more of a long, rambling run on sentence.

To test: Run MDict.py using python 3. It must be in the same folder containing "stories". The program will create a file called "output.txt"

