"""Generate Markov text from text files."""

from random import choice
import sys

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    open_and_read_file(input_path)
    """
    #return open(file_path).read()
    txt = open(sys.argv[1]).read()
    return txt
    #return 'Contents of your file as one long string'


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:
        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    word = text_string.split()
    for i in range(len(word) - 2):
        word_tuple = (word[i], word[i + 1])
        if word_tuple not in chains:
            chains[word_tuple] = []
            #word[i+2] == 'Would'
            #{('a', 'fox?'): []}
            #{('a', 'fox?'): ['Would']}
        chains[word_tuple].append(word[i + 2])
    return chains

def make_text(chains):
    """Return text from chains."""
    #create a key from our dictionary and a random word from the list of words that follow it
    #keys() doesnt return a list, use list() constructor to convert it
    #chains is our dictionary, pick random key/word from chains.keys()

    key = choice(list(chains.keys())) #chains is our dictionary, pick random key/word from chains.keys()
    #output: {('a', 'fox?'): ['Would']}
    words = [key[0], key[1]] #current output: {dict[key], rand_word} || {('a', 'fox?'): []}
    word = choice(chains[key]) #{('a', 'fox?'): ['Random']} >> pick random word from chains[key]

    #begin on a capital letter and end only at an instance of sentence punctuation
    while key[0][0].isupper():
        key = choice(key)
    # while chains.get(key):
    #     try:
    #         word = choice(chains[key])
    #         words.append(word)
    #         key = (key[1], word)
    #     except:
    #         raise KeyError
    # return ' '.join(words)

    while chains.get(key):
        if key in chains:
            word = choice(chains[key])
            words.append(word)
            key = (key[1], word)
        else:
            break
    return ' '.join(words)

input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
