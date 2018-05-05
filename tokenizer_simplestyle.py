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
            # i = word_tokenize(i)
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
                        # print(worktext[:5])


        # print(type(tokens))


def custom_sentence_devider(text, outfile):

    ''' takes a text as a long string and inserts new lines
        after periods at the end of sentences
        writes in new file
        created for Francke_trennung project
    '''

    with open(text, 'r') as openText:
        read_text = openText.read()

        with open(outfile, 'w') as newfile:

            read_text = read_text.replace('.', '.\n\n')

            newfile.write(read_text)
            # for i in read_text:
                # newfile.write(i)


    print(len(read_text), type(read_text))

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
                # lines.append(line)

                # lines.append(line)

                # unik_lines = set(lines)
                if len(line)>10:
                    # if line not in outfile:
                # for item in unik_lines:
                    # lines.append(line)
                    outfile.write(line)
                    # print(len(outfile))

                    # for i in lines:
    # return lines
                    # outfile.write(i)

    outfile.close()

# http//www.euro.who.int/__data/assets/pdf_file///RoadmapimplementTBCactionplan.pdf
# http//www.euro.who.int/__data/assets/pdf_file///EHREng.pdf
#<U+0080><U+0089>>â<U+0080><U+0089>

# my_sent_tokenizer(infile, outfile)
# my_word_tokenizer(infile, outfile)
# custom_sentence_devider(infile, outfile)
data_cleanup(infile, outfile)
