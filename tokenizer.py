import sys
import nltk
from nltk.tokenize import word_tokenize
from nltk import sent_tokenize

def my_sent_tokenizer(text, output):

    '''open file and turn it into a string'''

    with open(text, 'r') as myfile:

        read_string = myfile.read()

        sentences = sent_tokenize(read_string)

        dataset = open(output, 'w')

        for i in sentences:
            # i = word_tokenize(i)
            dataset.write(i+'\n')

    dataset.close()
    # print("what is datset", type(dataset))

    # return dataset

def my_word_tokenizer(text):

        my_sent_tokenizer(sys.argv[1], sys.argv[2])


        # worktext = open(text, 'r')

        read_worktext = text.read()

        tokens = word_tokenize(read_worktext)

        return tokens

print(type(my_sent_tokenizer(sys.argv[1], sys.argv[2])))

my_word_tokenizer(my_sent_tokenizer(sys.argv[1], sys.argv[2]))
