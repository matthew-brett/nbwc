#!/usr/bin/env python

from pathlib import Path
from argparse import ArgumentParser, RawDescriptionHelpFormatter

from nltk.tokenize import RegexpTokenizer
import jupytext


def wc_nb(fname):
    nb = jupytext.read(fname)
    tokenizer = RegexpTokenizer(r'\w+')
    word_counts = 0
    for cell in nb['cells']:
        if cell['cell_type'] != 'markdown':
            continue
        tokens = tokenizer.tokenize(cell['source'])
        word_counts += len(tokens)
    return word_counts


def get_parser():
    parser = ArgumentParser(description=__doc__,  # Usage from docstring
                            formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument('nb_fname',
                        help='Notebook filename')
    return parser


def main():
    parser = get_parser()
    args = parser.parse_args()
    print(f'Wordcount for {args.nb_fname}:', wc_nb(args.nb_fname))


if __name__ == '__main__':
    main()
