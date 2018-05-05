import sys
import nltk
import re
from nltk.tokenize import word_tokenize
from nltk import sent_tokenize

infile = sys.argv[1]
outfile = sys.argv[2]

def my_sent_tokenizer(infile, outfile):

    '''open file and turn it into a string'''

    with open(infile, 'r') as myfile:

        read_string = myfile.read()

        sentences = sent_tokenize(read_string)

        dataset = open(outfile, 'w')

        for i in sentences:

            dataset.write(i+'\n')

    dataset.close()

def my_word_tokenizer(infile, outfile):

        with open(infile, 'r') as worktext:


            # read_text = worktext.read()
            with open(outfile, 'w') as tokens:
                for sent in worktext:
                    sent = word_tokenize(sent)
                    for i in sent:
                        tokens.write(i+' ')
                    tokens.write('\n')


def data_cleanup(dataset, output):
    with open(dataset, 'r')as datatext:
        read = set(datatext.readlines())
        print(type(read), len(read))

        with open(output, 'w') as outfile:
            # lines =[]

            for line in read:
                line = re.sub(r'[\(\)\[\]\-\:\;\d]','',line)
                line = re.sub(r'\.\.\.','.', line)
                line = re.sub(r'\bhttps?\/\/.*[\r\n]*', '', line)
                line = re.sub(r'\= \.', '', line)
                line = re.sub(r'[%+≤-]','',line)
                line = re.sub(r'([\,\.]) [\.\,]+', '\1', line)
                line = re.sub(r'\s*\-\.\s*','', line)
                line = re.sub(r'<U+\d+\w*>', '', line)

                if len(line)>10:

                    outfile.write(line)

    outfile.close()


# my_sent_tokenizer(infile, outfile)
# my_word_tokenizer(infile, outfile)
data_cleanup(infile, outfile)
