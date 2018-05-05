import sys
import glob
import shutil

directory = sys.argv[1]
corpus = sys.argv[2]


def join_pages(sep_fns, dehyph_stream):
    """Concatenates several files into one.

    sep_fns: file or directory to be imported
    dehyph_stream: name of output file

    Define a directory containing the files to be concatenated in the first
    argument. Set the name of the output file as the second argument.
    The output file will be saved in the same directory.
    """
    # https://stackoverflow.com/questions/17749484/python-script-to-concatenate-all-the-files-in-the-directory-into-one-file
    with open(dehyph_stream, 'w') as outfile:
        # https://stackoverflow.com/questions/4813061/nonalphanumeric-list-order-from-os-listdir-in-python
        for filename in sorted(glob.glob(sep_fns + '/*.txt')):
            with open(filename, 'r') as readfile:
                shutil.copyfileobj(readfile, outfile)





join_pages(directory, corpus)
